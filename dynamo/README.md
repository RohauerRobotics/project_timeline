**3D Printed Dynamo Project**

**Software:** Fusion 360

**Time:** November through December 2019

The dynamo project was another of my early projects that went through multiple iterations. The original intention was to make a brushed dc motor with a 3D printed casing, while this wasn’t achieved a reasonably effective dynamo was made and one day I hope to finish this project and make a working motor (but will probably use a brushless design). 

**Design 1 - Uninformed Optimism** 

 <p align="center">
   <img src="https://github.com/RohauerRobotics/project_timeline/blob/main/dynamo/CAD%20Design%201%20-%20Whole.JPG" align="centre" width="50%" height="50%">
 </p>

My first design was based on no known theoretical knowledge about electronics or magnetism. It used a set of cylindrical rotors, which were composed of thinly wound bare wire around a 3D printed core of plastic, these rotors were placed with the central axis collinear to the long side of a set of rectangular permanent neodymium magnets. This design had no hope of actually working since there was no insulation of the wires, even if there was insulation the direction of the magnetic field from them would’ve been perpendicular to the direction of the permanent magnet’s field, and finally the bare wire was only wound once around the core so even in the optimal case the field strength would’ve been weak.



**Design 2 - Dynamo Prototype**

My second design addressed some of the basic errors that I made with my first design. I switched to thicker magnetic wire (wire with light insulation), I changed the dynamo configuration such that the rotor used a set of permanent magnets in the center, and I changed the coiled wire configuration such that if a current was passed through the wire the magnetic field would point in the same direction as the permanent magnets. 


The result produced an alternating current as the axle was turned, which means it was a reasonably successful endeavor. 
 
**Design 3 - Another Brushed DC Motor Attempt**



The final iteration I made was an attempt to adapt my brushed DC motor design with the lessons I had learned so far. I used the coils that induced a magnetic field in the correct direction (with the correct wire type), I reduced the distance between the electromagnets and permanent magnets so the strength wouldn’t decay too much, and I tried to make a commutator design so that the motor would spin with just a simple direct current applied. My design was ultimately unsuccessful. I think there were a few reasons why my design didn’t work. First was the commutator which wasn’t properly wired to the terminals of the coil bundles and didn’t maintain connection to the power source well. Another reason I think this didn’t work was because the material about which the electromagnetic coils were wound was steel and the permanent magnets were strongly attracted to the rotor which practically fixed it in place, and even when a current was sent through the coil, the magnetic field that was induced wasn’t strong enough to overcome this holding force.


While I never finished this project, it served as an introduction to electromagnetism and gave me an opportunity to iterate on a complex multipart assembly. Hopefully one day I’ll finish this project and be able to integrate custom motors into my projects. 
