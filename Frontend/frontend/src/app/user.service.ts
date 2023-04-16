import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  users = [
    {
      username: "admin",
      status: "online",
      contacts: ["friend"],
      past_chats: ["123","456","789"]
    },
    {
      username: "friend",
      status: "offline",
      contacts: [],
      past_chats: ["456"]
    }
  ];
  currentUser: string = '';
  private urlStub: string = 'http://localhost:8000/accounts'
  constructor(private http: HttpClient) { }

  getAll() {
    return this.users;
  }

  get(username: string) {
    for (var user of this.users) {
      if (user.username == username) {
        return user
      }
    }
    return
  }

  getHTTP(username: string) {
    return this.http.get<User>(this.urlStub+'/'+username);
  }
  
  add(user: any) {
    this.users.push(user);
  }

  addContact(username: string, contact: string) {
    for (var user of this.users) {
      if (user.username == username) {
        user.contacts.push(contact)
      }
    }
  }

  delete(user: any) {
    const index = this.users.indexOf(user)
    if (index >= 0) {
      this.users.splice(index, 1)
    }
  }

  getUsernames() {
    return ['admin','friend']
  }

  verifyPassword(username: string, password: string) {
    return true;
  }

  setCurrentUser(username: string) {
    this.currentUser = username;
  }

  getCurrentUser() {
    return this.currentUser;
  }

  isLoggedIn(): boolean {
    return this.currentUser == '' ? false : true;
  }
}

interface Contact {
  contact: string;
  id: number;
}

interface PastChat {
  pastChatID: number;
  id: number;
}

interface User {
  username: string;
  status: string;
  contacts: Contact[];
  pastChats: PastChat[];
}
