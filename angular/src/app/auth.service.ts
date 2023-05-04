import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';

interface LoginResponse {
  token: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly apiUrl = 'http://localhost:8000/api/';

  constructor(private http: HttpClient) { }

  login(email: string, password: string) {
    return this.http.post<LoginResponse>(`${this.apiUrl}auth/token/`, { email, password })
      .pipe(
        tap(response => {
          localStorage.setItem('token', response.token);
        })
      );
  }

  isAdmin() {
    const token = localStorage.getItem('token');
    if (!token) {
      return false;
    }
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload['is_staff'];
  }

  logout() {
    localStorage.removeItem('token');
  }
}
