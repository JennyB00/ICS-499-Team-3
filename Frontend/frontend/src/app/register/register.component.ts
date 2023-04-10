import {Component} from '@angular/core';
import { Router } from '@angular/router';

@Component({
    selector: 'app-register',
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.css']
})
export class RegisterComponent {
    registrationComplete: boolean = false;

    constructor(private router: Router) {}

    onRegistrationComplete() {
        this.registrationComplete = true;
    }

    toLoginPage() {
        //navigate to the login page
        this.router.navigate(['/login']);
    }
}