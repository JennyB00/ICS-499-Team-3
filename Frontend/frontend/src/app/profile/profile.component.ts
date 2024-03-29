import { Component, Input, OnInit } from '@angular/core';
import { Contact, User, UserService } from '../user.service';
import { AbstractControl, AsyncValidatorFn, FormArray, FormBuilder, FormControl, FormGroup, ValidationErrors, ValidatorFn, Validators} from '@angular/forms';
import { Router } from '@angular/router';
import { ChatService, Privileges } from '../chat.service';
import { Observable, map } from 'rxjs';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  // @Input() username: string;
  userHTTP: User;
  contacts: Contact[];
  pastChatUsers: Map<number,string[]> = new Map<number,string[]>();
  updatePassword: boolean = false;
  showContacts: boolean = false;
  addContact: boolean = false;
  deleteContact: boolean = false;
  newChat: boolean = false;
  passwordForm: FormGroup;
  contactForm: FormGroup;
  chatForm: FormGroup;
  
  constructor(
    private userService: UserService,
    private chatService: ChatService,
    private formBuilder: FormBuilder,
    private router: Router) {}
    
  ngOnInit(): void {
    if (!this.userService.isLoggedIn()) {
      this.router.navigate(['/']);
    }
    else {
      this.userService.getHTTP(this.userService.getCurrentUser()).subscribe((user) => {
        this.userHTTP = user;
        this.contacts = this.userHTTP.contacts;
        for (let pastChat of user.past_chats) {
          this.chatService.getUsers(pastChat.past_chat_id).subscribe((users) => {
            this.pastChatUsers.set(pastChat.past_chat_id, users);
          });
        }
        this.chatForm = this.formBuilder.group({
          users: this.formBuilder.array([
          ])
        });
        this.contacts.forEach(() => 
          this.users.push(this.formBuilder.control(false))
        );
        const existingContactValidator: ValidatorFn = (control: AbstractControl): ValidationErrors | null => {
          const contact = control.value;
          let contactUsernames: string[] = [];
          this.contacts.forEach((c) => {
            contactUsernames.push(c.contact);
          });
          return contactUsernames.indexOf(contact) > -1 ? {existing: true} : null;
        }
        this.contactForm = this.formBuilder.group({
          contact: this.formBuilder.control("",
          [Validators.required, existingContactValidator],
          this.contactValidator)
        });
      });
    }
    this.passwordForm = this.formBuilder.group({
      password: this.formBuilder.control("", [Validators.required, Validators.pattern('^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{5,}$')]),
      confirm: this.formBuilder.control("", Validators.required)
    }, {validators: confirmPasswordValidator});
  }
  contactValidator: AsyncValidatorFn = (control: AbstractControl): Observable<ValidationErrors | null> => {
    return this.userService.validUsername(control.value).pipe(
      map((valid) => valid ? {missing:true} : null)
      );
  }
  
  get users() {
    return this.chatForm.get('users') as FormArray;
  }
    
  onSubmitPassword(value: any) {
    const username = this.userService.getCurrentUser();
    const password = value.password;
    this.userService.updatePassword(username, password).subscribe();
    this.updatePassword = false;
  }
  onSubmitContact(value: any) {
    const contact = value.contact;
    this.userService.addContact(this.userHTTP.username,contact).subscribe(() => {
      this.userService.getContacts(this.userHTTP.username).subscribe((contacts) => {
        this.contacts = contacts;
      });
    });
    this.addContact = false;
  }
  onSubmitChat(value: any) {
    console.log(value);
    const values = value.users;
    const usernames: string[] = [];
    values.forEach((val:boolean, i:number) => {
      if (val) {
        const contact: Contact | undefined = this.contacts.at(i);
        if (contact) {
          usernames.push(contact.contact);
        }
      }
    });
    console.log(usernames);
    this.chatService.addChat(this.userHTTP.username).subscribe((response) => {
      console.log(response);
      const chat_id = response.id;
      for (let user of usernames){
        const newUser: Privileges = {
          username: user,
          send: true,
          receive: true,
          add_user: true,
          delete_message: false,
          delete_chat: false,
          id: chat_id
        };
        this.chatService.addPrivileges(chat_id, newUser).subscribe((response) =>{
          console.log(response);
        });
        this.userService.addPastChat(user, chat_id).subscribe(() => {
          
        });
      }
      this.userService.addPastChat(this.userService.getCurrentUser(),chat_id).subscribe((response2) => {
        console.log(response2);
        this.chatService.setChatID(chat_id);
        this.router.navigate(['/chat']);
      });
    });
    this.newChat = false;
  }
  onUpdatePassword() {
    this.updatePassword = true;
  }
  onCancelPassword() {
    this.updatePassword = false;
  }
  onShowContacts() {
    this.showContacts = true;
  }
  onHideContacts() {
    this.showContacts = false;
  }
  onAddContact() {
    this.addContact = true;
  }
  onCancelContact() {
    this.addContact = false;
  }
  onRequestDeleteContact() {
    this.deleteContact = true;
  }
  onCancelDeleteContact() {
    this.deleteContact = false;
  }
  onAddChat() {
    this.newChat = true;
  }
  onCancelChat() {
    this.newChat = false;
  }
  onChatClick(chatID: number) {
    this.chatService.setChatID(chatID);
    this.router.navigate(['/chat'])
  }
  onDeleteContact(contactID: number) {
    this.userService.deleteContact(contactID).subscribe(() => {
      this.contacts.splice(this.contacts.findIndex((value: Contact) => {return value.id == contactID}),1);
    });
    this.deleteContact = false;
  }
  getChatUsers(id: number) {
    let users;
    this.chatService.getUsers(id).subscribe((usernames) => {
      users = usernames;
    });
    return users;
  }
}

export const confirmPasswordValidator: ValidatorFn = (control: AbstractControl): ValidationErrors | null => {
  const password = control.get('password')?.value;
  const confirm = control.get('confirm')?.value;
  return password == confirm ? null : {notSame: true};
}