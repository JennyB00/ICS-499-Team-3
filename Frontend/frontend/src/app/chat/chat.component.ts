import { Component, OnInit } from '@angular/core';
import { MessageComponent } from '../message/message.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit{
  chatMessage: string;
  messages: string[] = [];
  privileges = []
  active = []

  constructor(private router: Router) {}

  homePage() {
    // navigate to the home page
    this.router.navigate(['/home']);
  }

  chatSettings() {
    // navigate to the home page
    this.router.navigate(['/chatSettings']);
  }

  sendMessage() {
    if (this.chatMessage) {
      this.messages.push(this.chatMessage);
      this.chatMessage = '';
    }
  }

  ngOnInit(): void {
    this.messages = []
  }

}
