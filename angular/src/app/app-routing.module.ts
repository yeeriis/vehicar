import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminComponent } from './admin/admin.component';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { LoginComponent } from './login/login.component';
import { CarsCardsComponent } from './cars-cards/cars-cards.component';
import { CarDetailComponent } from './car-detail/car-detail.component';
import { UserRegisterComponent } from './user-register/user-register.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { MainCarrouselComponent } from './main-carrousel/main-carrousel.component';
import { HomeComponent } from './home/home.component';
import { CarLeasingComponent } from './car-leasing/car-leasing.component';



const routes: Routes = [
  {
    path: 'admin',
    component: AdminComponent
  },
  {
    path: 'login-admin',
    component: AdminLoginComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: '',
    component: HomeComponent
  },
  
  {
    path: 'coches/:id',
    component: CarDetailComponent
  },
  {
    path: 'register',
    component: UserRegisterComponent
  },
  {
    path: 'profile',
    component: UserProfileComponent
  },
  {
    path: 'llogar/:id',
    component: CarLeasingComponent
  }
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
