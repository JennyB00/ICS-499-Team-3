import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpParams } from '@angular/common/http';
import { UserService } from '../user.service';

@Component({
  selector: 'app-bot',
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css']
})

export class BotComponent implements OnInit{
  messages: listItem[] = [];
  newMessage = '';

  constructor(private router: Router, private http: HttpClient, private userService: UserService) {}

  ngOnInit(): void {
    if (!this.userService.isLoggedIn()) {
      this.router.navigate(["/"]);
    }
  }

  // homePage() {
  //   // navigate to the home page
  //   this.router.navigate(['/home']);
  // }

  submit() {
    if (this.newMessage.trim() !== '') {
      // send the message to the server using POST request
      this.messages.push({type: "prompt",message: this.newMessage});
      this.http.post('http://localhost:8000/bot/process','', { params: new HttpParams().set('prompt',this.newMessage).set('username',this.userService.getCurrentUser())})
        .subscribe({
          next: (response) => {
            console.log('Message sent successfully');
            console.log('Response:', response);
            this.messages.push({type: "response",message: response.toString()});
            this.newMessage = '';
          },
          error: (error) => {
            console.error('Error sending message: ', error);
            console.log('Error response body: ', error.error);
          }
        });
    }
  }

  onKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter' && this.newMessage.trim() !== '') {
      this.submit();
    }
  }
}

interface listItem {
  type: string;
  message: string;
}