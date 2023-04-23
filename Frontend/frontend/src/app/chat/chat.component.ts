import { Component, OnInit } from '@angular/core';
import { MessageComponent } from '../message/message.component';
import { Router } from '@angular/router';
import { Chat, ChatService, Message, MessageCreate } from '../chat.service';
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
  messages: string[];
  // privileges = [];
  // active = [];
  private encoder = new TextEncoder();

  constructor(private chatService: ChatService,
    private userService: UserService,
    private router: Router) {}

  ngOnInit(): void {
    this.messages = [];
    if (this.chatService.isChatSelected()) {
      const id = this.chatService.getChatID();
      this.chatService.getChat(id).subscribe((chat) => {this.chat = chat});
      for (let m of this.chat.messages) {
        this.messages.push(m.username+': '+m.message.toString());
      }
    } else {
      this.messages = [];
    }
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

  sendStringMessage() {
    const id = this.chatService.getChatID();
    const message: MessageCreate = {
      username: this.userService.getCurrentUser(),
      type: "str",
      date: new Date().toISOString(),
      message: this.chatMessage
    };
    this.chatService.addMessage(id,message).subscribe(() => { this.chatMessage = ''; });
    this.messages.push(this.chatMessage);
  }
}
