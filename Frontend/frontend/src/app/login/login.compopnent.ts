import {Component, EventEmitter, Output} from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  // @Output() login = new EventEmitter();
  loginFailure: boolean = false;

  constructor(private userService: UserService, private router: Router) {}
  // onLoginFailure() {
  //   this.loginFailure = true;
  // }
  // onLoginSuccess() {
  //   this.login.emit()
  // }
  onSubmit(value: any) {
    const username = value.username;
    const password = value.password;
    if (this.userService.verifyPassword(username, password)) {
      this.userService.setCurrentUser(username);
      this.router.navigate(['/profile']);
    } 
    else {
      this.loginFailure = true;
    }
  }
}