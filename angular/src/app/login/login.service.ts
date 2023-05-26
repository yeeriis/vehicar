import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }

  logueo(email: string, password: string) {
    const body = { email, password };
    return this.http.post('/api/login', body);
  }
}
