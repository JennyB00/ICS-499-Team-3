import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-bot',
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css']
})

export class BotComponent {
  messages: string[] = [];
  newMessage = '';

  constructor(private router: Router) {}

  homePage() {
    // navigate to the home page
    this.router.navigate(['/home']);
  }

  submit() {
    if (this.newMessage.trim() !== '') {
      this.messages.push(this.newMessage);
      this.newMessage = '';
    }
  }
}
