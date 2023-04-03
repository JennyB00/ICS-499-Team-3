import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  @Input() user: any;
  updateUsername: boolean = false;
  updatePassword: boolean = false;
  showContacts: boolean = false;
  onUpdateUsername() {
    this.updateUsername = true;
  }
  onUpdatePassword() {
    this.updatePassword = true;
  }
  onShowContacts() {
    this.showContacts = true;
  }
  onHideContacts() {
    this.showContacts = false;
  }
}
