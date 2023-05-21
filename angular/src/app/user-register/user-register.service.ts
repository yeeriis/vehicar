import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserRegisterService {
  private url = 'http://localhost:8000/api/register/';

  constructor(private http: HttpClient) { }

  registrarUsuario(usuario: any) {
    return this.http.get(this.url, usuario);
  }
}
