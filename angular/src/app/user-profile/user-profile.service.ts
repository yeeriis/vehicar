import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class UserProfileService {

  constructor(private http: HttpClient) { }

  getUserDetails(){
    return this.http.get('http://localhost:8000/api/usuario')
  }
}
