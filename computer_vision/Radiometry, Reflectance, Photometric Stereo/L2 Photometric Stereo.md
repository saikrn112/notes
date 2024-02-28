![[why_photometric_stereo.png|300]]
shape from intensities 

![[photostereo_topics.png]]

 ![[photo_stereo_known_unknown.png]]

measure surface normals given other quantitites


![[surface_normals.png]]
![[gradient_space.png]]

![[reflectance_map.png]]

We get below formulations from [[L1 Radiometric Concepts#^b39f62|here]] 

![[reflectance_map_lambertian_surface.png]]

![[reflectance_lambertion_2.png]]

![[reflectance_lambertian_iso_cont1.png]]
![[reflectance_lambertian_iso_cont2.png]]


can we estimate the surface normal given image intensity and other parameters from this ? 
NO!!! 
because of iso contours we can have many solutions
idea of the photometric stereo is disambiguate this by using different lighting conditions


![[photometric_stereo_1.png]]

![[photometric_stereo_example.png]]

![[photo_stereo_basic_idea2.png]]
worst case is for specular since each light source direction maps to only 1 point 
so need infinite light sources!!


----

Lambertian Case
![[albedo.png]]

![[photometric_stereo_lambertian_case1.png]]
![[photometric_stereo_lambertian_case2.png]]
with just 3 different viewing directions we can figure out the entire properties of lambertian surface

![[photometric_stereo_lambertian_case4.png]]

>[!info] All hail Sun!
>let sun do the job of different lighting conditions for outdoors. 
>all you gotta do is collect images at different times

![[photometric_stereo_lambertian_case5.png]]

better normals esimation for a point? 
![[photometric_stereo_lambertian_case6.png]]


![[effective_point_source_only_for_lambertian.png]]


![[photometric_stereo_results1.png|200]]![[photometric_stereo_results2.png|200]]
![[photometric_stereo_results3.png]]
clearly we cant asume everything to be lambertian since the above toy albedo was not accurate. it clearly has reflections so calibrated photometric stereo

-----

![[calibrated_photometric_stereo.png]]

![[calibration_photometric_stereo.png]]

![[calibration_photometric_stereo-1.png]]
![[calibrated_photometric_stereo-1.png]]

----

## Integrating 3D normals for shape
smooth and continuous object (no disctunuities)
![[shape_from_normals-1.png]]
if the surface normals computed is correct then taking any path makes sense (and assuming surface is smooth)
![[shape_from_normals-2.png]] 

![[surface_from_normals.png]]

![[surface_from_normals-1.png]]

Elegant way of estimating surface shape in presense of noise
![[surface_from_normals-2.png]]


![[surface_from_normals-3.png]]
![[surface_from_normals-4.png]]

![[surface_from_normals-5.png]]
![[surface_from_normals-6.png]]
![[surface_from_normals-7.png]]

-----

## Interreflections

![[interreflection.png]]

>[!info] interreflection issue
>albedo is overestimated because more light 
>surface tilt is underestimated because brighter values are closer to the light source  


![[interreflection-1.png]]