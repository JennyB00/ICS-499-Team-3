import { Component, Input, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { AbstractControl, FormBuilder, FormControl, FormGroup, ValidationErrors, ValidatorFn, Validators} from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  // @Input() username: string;
  user: any;
  updateUsername: boolean = false;
  updatePassword: boolean = false;
  showContacts: boolean = false;
  addContact: boolean = false;
  addChat: boolean = false;
  usernameForm: FormGroup;
  passwordForm: FormGroup;
  contactForm: FormGroup;
  chatForm: FormGroup;
  
  constructor(
    private userService: UserService,
    private formBuilder: FormBuilder,
    private router: Router) {}
    
  ngOnInit(): void {
    if (!this.userService.isLoggedIn()) {
      this.router.navigate(['/']);
    }
    else {
      this.user = this.userService.get(this.userService.getCurrentUser());
    }
    this.usernameForm = this.formBuilder.group({
      username: this.formBuilder.control("", Validators.required)
    });
    this.passwordForm = this.formBuilder.group({
      password: this.formBuilder.control("", Validators.required),
      confirm: this.formBuilder.control("", Validators.required)
    }, {validators: this.confirmPasswordValidator});
    this.contactForm = this.formBuilder.group({
      contact: this.formBuilder.control("", Validators.required)
    });
    this.chatForm = this.formBuilder.group({
      users: this.formBuilder.control("")
    });
  }
  confirmPasswordValidator: ValidatorFn = (control: AbstractControl): ValidationErrors | null => {
    const password = control.get('password')?.value
    const confirm = control.get('confirm')?.value
    return password == confirm ? null : {notSame: true}
  }
    

  onSubmitUsername(value: any) {
    this.updateUsername = false;
  }
  onSubmitPassword(value: any) {
    this.updatePassword = false;
  }
  onSubmitContact(value: any) {
    this.addContact = false;
  }
  onSubmitChat(value: any) {
    this.addChat = false;
  }
  onUpdateUsername() {
    this.updateUsername = true;
  }
  onCancelUsername() {
    this.updateUsername = false;
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
  onChatClick(chatID: string) {
    this.router.navigate(['/chat'])
  }
  onBotClick() {
    this.router.navigate(['/bot'])
  }
}
