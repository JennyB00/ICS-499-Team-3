import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, ValidatorFn, AbstractControl, ValidationErrors, AsyncValidatorFn } from '@angular/forms';
import { UserCreate, UserService } from '../user.service';
import { Router } from '@angular/router';
import { Observable, map } from 'rxjs';
import { confirmPasswordValidator } from '../profile/profile.component';

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
                Validators.pattern('[\\w\\-\\s\\/]+')]),
                this.uniqueUsernameValidator),
            password: new FormControl('', Validators.compose([
                Validators.required,
                Validators.pattern('^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{5,}$')])),
            confirm: new FormControl('', Validators.compose([
                Validators.required]))
        },
        confirmPasswordValidator);
    }

    uniqueUsernameValidator: AsyncValidatorFn = (control: AbstractControl): Promise<ValidationErrors | null> | Observable<ValidationErrors | null> => {
        return this.userService.validUsername(control.value).pipe(
            map((valid) => valid ? null : {taken:true})
        );
    }

    onSubmit(value: any){
        const username: string = value.username;
        const password: string = value.password;
        if(this.registrationForm.valid){
            const newUser: UserCreate = {username: username, password: password, status: 'offline'};
            this.userService.add(newUser).subscribe(()=>{
                this.registrationComplete = true;
            });
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