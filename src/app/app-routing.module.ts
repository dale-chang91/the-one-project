import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

/**
 * Components for routing
 */
import { PlaceholderComponent } from './placeholder/placeholder.component';
import { EducationComponent } from './education/education.component';
import { NotFoundComponent } from './shared/not-found/not-found.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'placeholder',
    pathMatch: 'full'
  },
  {
    path: 'placeholder',
    component: PlaceholderComponent
  },
  {
    path: 'education',
    component: EducationComponent
  },
  {
    path: 'not-found',
    component: NotFoundComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
