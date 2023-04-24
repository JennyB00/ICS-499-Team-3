import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { UserCreate, UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
    selector: 'app-register',
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
    registrationComplete: boolean = false;
    registrationForm: FormGroup;
    usernameTaken: boolean = false;

    constructor(private userService: UserService, private router: Router) {}

    ngOnInit(){
        this.registrationForm = new FormGroup({
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

    onSubmit(value: any){
        const username: string = value.username;
        const password: string = value.password;
        const usernames = this.userService.getUsernames();
        for(var index in usernames){
            if(username == usernames[index]){
                this.usernameTaken = true;
                break;
            }
        }
        if(this.usernameTaken == false){
            const newUser: UserCreate = {username: username, password: password, status: 'offline'};
            this.userService.add(newUser);
            this.registrationComplete = true;
        }
    }

    onRegistrationComplete() {
        this.registrationComplete = true;
    }

    toLoginPage() {
        //navigate to the login page
        this.router.navigate(['/login']);
    }
}