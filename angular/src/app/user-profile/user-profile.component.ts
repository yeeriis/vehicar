import { Component, OnInit } from '@angular/core';
import { UserProfileService } from './user-profile.service';


@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  userProfileDetails: any; // Variable para almacenar los detalles del perfil del usuario

  constructor(private userProfileService: UserProfileService) {}

  ngOnInit() {
    this.userProfileService.getUserDetails().subscribe(
      (data) => {
        this.userProfileDetails = data; // Almacena los detalles del perfil del usuario en la variable
      },
      (error) => {
        console.log(error);
      }
    );
  }
}
