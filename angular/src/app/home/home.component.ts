import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent {
  items: any[];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<any[]>('/api/my-model/').subscribe(
      data => {
        this.items = data;
      },
      error => {
        console.error(error);
      }
    );
  }
}
