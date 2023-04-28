import { Component, EventEmitter, Output, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import { confirmPasswordValidator } from '../profile/profile.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  // @Output() login = new EventEmitter();
  loginFailure: boolean = false;
  loginForm: FormGroup;

  constructor(private userService: UserService, private router: Router) {}
  // onLoginFailure() {
  //   this.loginFailure = true;
  // }
  // onLoginSuccess() {
  //   this.login.emit()
  // }

  ngOnInit(){
    this.loginForm = new FormGroup({
      username: new FormControl('', Validators.compose([
        Validators.required,
        Validators.pattern('[\\w\\-\\s\\/]+')
      ])),
      password: new FormControl('', Validators.compose([
        Validators.required,
        Validators.pattern('[\\w\\-\\s\\/]+')
      ]))
    });
  }

  onSubmit(value: any) {
    const username: string = value.username;
    const password: string = value.password;
    this.userService.getPassword(username).subscribe((pass) => {
      const match: boolean = (pass == password);
      if (match) {
        this.userService.setCurrentUser(username);
        this.userService.updateStatus(username, 'online');
        this.router.navigate(['/profile']);
      }
      else {
        this.loginFailure = true;
      }
    });
    // if (this.userService.verifyPassword(username, password)) {
    //   this.userService.setCurrentUser(username);
    //   this.router.navigate(['/profile']);
    // } 
    // else {
    //   this.loginFailure = true;
    // }
  }
}