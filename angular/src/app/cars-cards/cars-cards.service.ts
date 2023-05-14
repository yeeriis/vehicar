import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class CarsService {
  apiUrl = 'http://localhost:8000/api/coches/';

  constructor(private http: HttpClient) { }

  getCars() {
    return this.http.get(this.apiUrl)
      .pipe(
        map((response: any) => {
          return response.coches;
        })
      );
  }

  
}
