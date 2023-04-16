import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { UserService } from '../user.service';

@Component({
  selector: 'app-bot',
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css']
})

export class BotComponent implements OnInit{
  messages: string[] = [];
  newMessage = '';

  constructor(private router: Router, private http: HttpClient, private userService: UserService) {}

  ngOnInit(): void {
    if (!this.userService.isLoggedIn()) {
      this.router.navigate(["/"]);
    }
  }

  submit() {
    console.log('Input was: ', this.newMessage)

    if (this.newMessage.trim() !== '') {
      // send the message to the server using POST request
      this.http.post('http://localhost:8000/bot/process', { prompt: this.newMessage})
        .subscribe({
          next: (response) => {
            console.log('Message sent successfully');
            console.log('Input was:', this.newMessage);
            console.log('Response:', response);
            this.messages.push(this.newMessage);
            this.newMessage = '';
          },
          error: (error) => {
            console.error('Error sending message: ', error);
            console.log('Error response body: ', error.error);
          }
        });
    }
  }
}