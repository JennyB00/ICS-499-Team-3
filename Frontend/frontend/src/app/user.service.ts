import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private currentUser: string = '';
  private urlStub: string = '/accounts/'
  constructor(private http: HttpClient) { }

  /**
   * Query the backend for all accounts with an optional limit
   * @param limit GET query option
   * @returns Observable of the backend HTTP GET
   */
  getAll(limit?: number) {
    const options = (typeof limit !== 'undefined') ? {params: new HttpParams().set('limit',limit)} : {};
    return this.http.get<User[]>(this.urlStub, options);
  }

  /**
   * Takes in an account to query the back end
   * @param username username for the account to query
   * @returns Observable of the backend HTTP GET
   */
  getHTTP(username: string) {
    return this.http.get<User>(this.urlStub+username);
  }

  /**
   * Creates an account in the backend
   * @param user interface with username, password, and status. This matches the
   * backend query parameters
   * @returns Observable of the backend HTTP POST
   */
  add(user: UserCreate) {
    return this.http.post<User>(this.urlStub, user);
  }

  /**
   * HTTP GET of validating new username is unique
   * @param username new username to validate it is unique
   * @returns Observable of boolean response
   */
  validUsername(username: string) {
    const options = {params: new HttpParams().set('username', username)}
    return this.http.get<boolean>(this.urlStub+'valid_username', options);
  }

  /**
   * Sends a delete to the backend of the given user
   * @param username user to delete
   * @returns Obervable of backend HTTP DELETE success message
   */
  delete(username: string) {
    return this.http.delete<messageResponse>(this.urlStub+username);
  }

  verifyPassword(username: string, password: string) {
    let match: boolean;
    this.http.get<string>(this.urlStub+username+'/password').subscribe((pass) => {match = (pass == password); return match;});
    return true;
  }

  /**
   * Queries backend for password
   * @param username user to grab password of
   * @returns Observable of account password
   */
  getPassword(username: string) {
    return this.http.get<string>(this.urlStub+username+'/password');
  }

  /**
   * HTTP POST to update user's password
   * @param username user to update password for
   * @param password new password
   * @returns Observable of successful message
   */
  updatePassword(username: string, password: string) {
    const options = { params: new HttpParams().set('password',password) };
    return this.http.post<messageResponse>(this.urlStub+username+'/password', '', options);
  }

  /**
   * HTTP POST to update user status
   * @param username user to update the status of
   * @param status the new status, only online or offline
   * @returns Observable of the successful message
   */
  updateStatus(username: string, status: string) {
    const options = { params: new HttpParams().set('status',status) };
    return this.http.post<messageResponse>(this.urlStub+username+'/status', '', options);
  }

  /**
   * HTTP GET a user's contacts
   * @param username user to get contacts of
   * @returns Observable of Contact list
   */
  getContacts(username: string) {
    return this.http.get<Contact[]>(this.urlStub+username+'/contacts');
  }

  /**
   * Adds a contact to the given user
   * @param username user to add contact to
   * @param contact contact to add
   * @returns Observable of new Contact
   */
  addContact(username: string, contact: string) {
    const options = { params: new HttpParams().set('contact',contact) };
    return this.http.post<Contact>(this.urlStub+username+'/contacts','',options);
  }

  /**
   * HTTP DELETE of a contact from the backend
   * @param id ID of the contact to delete
   * @returns Observable of success message
   */
  deleteContact(id: number) {
    return this.http.delete<messageResponse>('/contacts/'+id);
  }

  /**
   * HTTP POST to add a chat id to a user's past chats
   * @param username user to add past chat to
   * @param chatID past chat ID
   * @returns Observable of new PastChat
   */
  addPastChat(username: string, chatID: number) {
    const options = { params: new HttpParams().set('past_chat_id',chatID) };
    return this.http.post<PastChat>(this.urlStub+username+'/past_chats','',options);
  }

  /**
   * HTTP DELETE to remove the given PastChat
   * @param id ID of past chat id to remove
   * @returns Observable of success message
   */
  deletePastChat(id: number) {
    return this.http.delete<messageResponse>('/past_chats/'+id);
  }

  /**
   * Sets the currently logged in user for components to grab. 
   * Set this to '' when logging out
   * @param username user logging in
   */
  setCurrentUser(username: string) {
    this.currentUser = username;
  }

  /**
   * Get the username of the currently logged in user
   * @returns username of the currently logged in user
   */
  getCurrentUser() {
    return this.currentUser;
  }

  /**
   * Simplest security flag. Assumes that a blank current user
   * means the user is not logged in
   * @returns true if user is logged in, false otherwise
   */
  isLoggedIn(): boolean {
    return this.currentUser == '' ? false : true;
  }
}

export interface Contact {
  contact: string;
  id: number;
}

interface PastChat {
  past_chat_id: number;
  id: number;
}

interface UserBase {
  username: string;
  status: string;
}

export interface User extends UserBase {
  contacts: Contact[];
  past_chats: PastChat[];
}

export interface UserCreate extends UserBase {
  password: string;
}

export interface messageResponse {
  message: string;
}
