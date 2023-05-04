import { Component } from '@angular/core';
import { AuthService } from '../auth.service';


@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})

export class AdminComponent {
  constructor(private authService: AuthService) {}

  ngOnInit() {
    if (!this.authService.isAdmin()) {
      alert('You are not authorized to access this page.');
      this.authService.logout();
    }
  }
}
