import { Component, OnInit } from '@angular/core';
import { MessageComponent } from '../message/message.component';
import { Router } from '@angular/router';
import { Chat, ChatService, Message, MessageCreate, Privileges, PrivilegesCreate } from '../chat.service';
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
  selectedUser: string;
  messages: Message[];
  privileges: Privileges;
  active: string[];
  deleteMessage: boolean = false;
  chatSettings: boolean = false;
  deleteChat: boolean = false;
  addUser: boolean = false;
  removeUser: boolean = false;

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

  onChatSettings() {
    const flip: boolean = !this.chatSettings;
    this.chatSettings = flip;
  }

  onDeleteMessage() {
    this.deleteMessage = true;
  }

  submitDeleteMessage(messageID: number) {
    this.chatService.deleteMessage(messageID).subscribe((response) => {
      console.log(response);
      this.deleteMessage = false;
    });
  }

  cancelDeleteMessage() {
    this.deleteMessage = false;
  }

  onDeleteChat() {
    this.deleteChat = true;
  }

  submitDeleteChat(chatID: number) {
    this.chatService.deleteChat(chatID).subscribe((response) => {
      console.log(response)
      this.deleteChat = false;
      this.router.navigate(['/profile']);
    });
  }

  cancelDeleteChat() {
    this.deleteChat = false;
  }

  onAddUser(){
    this.addUser = true;
  }

  submitAddUser(){
    const newUser: PrivilegesCreate = {
      username: this.selectedUser,
      send: true,
      receive: true,
      add_user: true,
      delete_message: false,
      delete_chat: false
    };
    this.chatService.addPrivileges(this.id, newUser).subscribe((response) => {
      console.log(response);
      this.selectedUser = '';
      this.addUser = false;
      this.userService.addPastChat(this.selectedUser, this.id).subscribe((response) => {
        console.log(response);
      });
    });
  }
  cancelAddUser() {
    this.addUser = false;
  }

  onRemoveUser(){
    this.removeUser = true;
  }

  //Not sure this is the correct way to remove users. might want to double check.
  submitRemoveUser(){
    let priv: Privileges | undefined;
    this.chat.privileges.forEach((p) => {
      if (p.username == this.selectedUser) {
        priv = p;
      }
    });
    if (priv) {
        this.chatService.deletePrivileges(priv.id).subscribe((response) => {
          console.log(response);
          this.selectedUser = '';
          this.removeUser = false;
        });
    }
  }

  cancelRemoveUser(){
    this.removeUser = false;
  }
}
