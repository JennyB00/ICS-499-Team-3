import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent {
  constructor(private router: Router) {}

  register() {
    // navigate to the registration page
    this.router.navigate(['/register']);
  }

  login() {
    // navigate to the login page
    this.router.navigate(['/login']);
  }
}
