import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private currentChatID: number = -1;
  private urlStub: string = 'http://localhost:8000/chats/'

  constructor(private http: HttpClient) { }

  isChatSelected(): boolean {
    return this.currentChatID < 0 ? false : true;
  }

  getChatID(): number {
    return this.currentChatID;
  }

  setChatID(id: number): void {
    this.currentChatID = id;
  }

  /**
   * HTTP GET for a given chat
   * @param id ID of the chat to get
   * @returns Observable of Chat request
   */
  getChat(id: number): Observable<Chat> {
    return this.http.get<Chat>(this.urlStub+id);
  }

  /**
   * HTTP POST to add a new chat by the given user
   * @param username creator user for highest privileges
   * @returns Observable of new Chat
   */
  addChat(username: string): Observable<Chat> {
    const options = { params: new HttpParams().set('username', username) };
    return this.http.post<Chat>(this.urlStub, '', options);
  }

  /**
   * HTTP DELETE request to backend
   * @param id ID of chat to delete
   * @returns Observable of success message
   */
  deleteChat(id: number): Observable<string> {
    return this.http.delete<string>(this.urlStub+id);
  }

  /**
   * HTTP GET request for a list of usernames of online users in the requested chat
   * @param id ID of chat to get active users for
   * @returns Observable of array of usernames for active users
   */
  getActive(id: number): Observable<string[]> {
    return this.http.get<string[]>(this.urlStub+id+'/active');
  }

  /**
   * HTTP POST
   * @param id ID of chat to add privileges to
   * @param privileges Privileges to add
   * @returns Observable of new Privilegs
   */
  addPrivileges(id: number, privileges: PrivilegesCreate): Observable<Privileges> {
    return this.http.post<Privileges>(this.urlStub+id+'/privileges',privileges);
  }

  /**
   * HTTP DELETE of privileges object to backend
   * @param id ID of privileges to delete
   * @returns Observable of success message
   */
  deletePrivileges(id: number): Observable<string> {
    return this.http.delete<string>('http://localhost:8000/privileges/'+id);
  }

  /**
   * HTTP POST
   * @param id ID of chat to add message to
   * @param message Message to add
   * @returns Observable of new Message
   */
  addMessage(id: number, message: MessageCreate): Observable<Message> {
    return this.http.post<Message>(this.urlStub+id+'/messages',message);
  }

  /**
   * HTTP DELETE of message object to backend
   * @param id ID of the message to delete
   * @returns Observable of success message
   */
  deleteMessage(id: number): Observable<string> {
    return this.http.delete<string>('http://localhost:8000/messages/'+id);
  }
}

interface PrivilegesCreate {
  username: string;
  send: boolean;
  receive: boolean;
  add_user: boolean;
  delete_message: boolean;
  delete_chat: boolean;
}

interface Privileges extends PrivilegesCreate {
  id: number;
}

export interface MessageCreate {
  username: string;
  date: string;
  type: string;
  message: string;
}

export interface Message extends MessageCreate {
  id: number;
}

export interface Chat {
  id: number;
  messages: Message[];
  privileges: Privileges[];
}