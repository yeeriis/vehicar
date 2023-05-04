import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from "rxjs/Observable";


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    return this.http.post(`${this.BASE_URL}/api/login/`, {
      username: username,
      password: password
    });
  }
}
