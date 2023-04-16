import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  constructor(private router: Router, private userService: UserService) {}

  loggedIn() {
    return this.userService.isLoggedIn();
  }

  onHome() {
    this.router.navigate(["/profile"]);
  }
  onAbout() {
    this.router.navigate(["/"]);
  }
  onLogin() {
    // navigate to the login page
    this.router.navigate(['/login']);
  }
}
