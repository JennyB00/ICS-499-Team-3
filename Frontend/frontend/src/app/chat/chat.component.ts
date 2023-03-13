import { Component, OnInit } from '@angular/core';
import { MessageComponent } from '../message/message.component';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit{
  messages = [MessageComponent]
  privileges = []
  active = []

  constructor() {}


  ngOnInit(): void {
    this.messages = []
  }



}
