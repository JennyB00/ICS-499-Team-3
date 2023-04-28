import { Component, OnInit } from '@angular/core';
import { MessageComponent } from '../message/message.component';
import { Router } from '@angular/router';
import { Chat, ChatService, Message, MessageCreate, Privileges } from '../chat.service';
import { UserService } from '../user.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit{
  chat: Chat;
  id: number;
  chatMessage: string;
  messages: Message[];
  privileges: Privileges;
  // active = [];

  constructor(private chatService: ChatService,
    private userService: UserService,
    private router: Router) {}

  ngOnInit(): void {
    this.messages = [];
    if (this.chatService.isChatSelected() && this.userService.isLoggedIn()) {
      const id = this.chatService.getChatID();
      this.chatService.getChat(id).subscribe((chat) => {
        this.chat = chat;
        this.messages = chat.messages;
        for (let p of chat.privileges) {
          if (p.username == this.userService.getCurrentUser()) {
            this.privileges = p;
          }
        }
        if (!this.privileges) {
          this.router.navigate(['/']);
        }
      });
    } else {
      this.router.navigate(['/']);
    }
  }

  chatSettings() {
    // navigate to the home page
    this.router.navigate(['/chatSettings']);
  }

  sendMessage() {
    // if (this.chatMessage) {
    //   this.messages.push(this.chatMessage);
    //   this.chatMessage = '';
    // }
  }

  sendStringMessage() {
    const id = this.chatService.getChatID();
    const message: MessageCreate = {
      username: this.userService.getCurrentUser(),
      type: "str",
      date: new Date().toISOString(),
      message: this.chatMessage
    };
    this.chatService.addMessage(id,message).subscribe((newMessage) => {
      this.chatMessage = '';
      this.messages.push(newMessage);
    });
  }
}
