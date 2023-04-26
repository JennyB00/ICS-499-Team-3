import { Component, Input, OnInit } from '@angular/core';
import { User, UserService } from '../user.service';
import { AbstractControl, AsyncValidatorFn, FormBuilder, FormControl, FormGroup, ValidationErrors, ValidatorFn, Validators} from '@angular/forms';
import { Router } from '@angular/router';
import { ChatService } from '../chat.service';
import { Observable, map } from 'rxjs';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  // @Input() username: string;
  userHTTP: User;
  updatePassword: boolean = false;
  showContacts: boolean = false;
  addContact: boolean = false;
  addChat: boolean = false;
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
      this.userService.getHTTP(this.userService.getCurrentUser()).subscribe((user) => {this.userHTTP = user} );
    }
    this.passwordForm = this.formBuilder.group({
      password: this.formBuilder.control("", [Validators.required, Validators.pattern('^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{5,}$')]),
      confirm: this.formBuilder.control("", Validators.required)
    }, {validators: this.confirmPasswordValidator});
    this.contactForm = this.formBuilder.group({
      contact: this.formBuilder.control("", Validators.required, this.contactValidator)
    });
    this.chatForm = this.formBuilder.group({
      users: this.formBuilder.control("")
    });
  }
  confirmPasswordValidator: ValidatorFn = (control: AbstractControl): ValidationErrors | null => {
    const password = control.get('password')?.value;
    const confirm = control.get('confirm')?.value;
    return password == confirm ? null : {notSame: true};
  }
  contactValidator: AsyncValidatorFn = (control: AbstractControl): Observable<ValidationErrors | null> => {
    return this.userService.validUsername(control.value).pipe(
        map((valid) => valid ? {missing:true} : null)
    );
}
    

  onSubmitPassword(value: any) {
    const username = this.userService.getCurrentUser();
    const password = value.password;
    this.userService.updatePassword(username, password).subscribe();
    this.updatePassword = false;
  }
  onSubmitContact(value: any) {
    const contact = value.contact;
    this.userService.addContact(this.userService.getCurrentUser(),contact).subscribe();
    this.addContact = false;
  }
  onSubmitChat(value: any) {
    this.addChat = false;
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
  onAddChat() {
    this.addChat = true;
  }
  onCancelChat() {
    this.addChat = false;
  }
  onChatClick(chatID: number) {
    this.chatService.setChatID(chatID);
    this.router.navigate(['/chat'])
  }
}
