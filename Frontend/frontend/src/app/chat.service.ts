import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor() { }
}

interface Privileges {
  username: string;
  send: boolean;
  receive: boolean;
  add_user: boolean;
  delete_message: boolean;
  delete_chat: boolean;
  id: number;
}

export interface Message {
  username: string;
  date: Date;
  type: string;
  message: BinaryType;
  id: number;
}

export interface Chat {
  id: number;
  messages: Message[];
  privileges: Privileges[];
}