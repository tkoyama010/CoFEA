# Elmer

Elmer supports elastic simulations out of the box. Below there is an explanation of solver input file.

```
Header
  CHECK KEYWORDS Warn
  Mesh DB "." "Mesh/cfa-fine-lin-hex"               # Path to the mesh
  Include Path ""
  Results Directory "Results/cfa-fine-lin-hex"      # Path to results directory
End

Simulation                                          # Settings and constants for simulation
  Max Output Level = 5
  Coordinate System = Cartesian
  Coordinate Mapping(3) = 1 2 3
  Simulation Type = Steady state
  Steady State Max Iterations = 1
  Output Intervals = 1
  Timestepping Method = BDF
  BDF Order = 1
  Solver Input File = case.sif
  Post File = case.vtu
End

Constants
  Gravity(4) = 0 -1 0 9.82
  Stefan Boltzmann = 5.67e-08
  Permittivity of Vacuum = 8.8542e-12
  Boltzmann Constant = 1.3807e-23
  Unit Charge = 1.602e-19
End

Body 1                                              # Assigning the material and equations to the mesh
  Target Bodies(1) = 1
  Name = "Body Property 1"
  Equation = 1
  Material = 1
End

Solver 1                                            # Solver settings
  Equation = Linear elasticity
  Calculate Loads = True
  Calculate Stresses = True
  Procedure = "StressSolve" "StressSolver"
  Variable = -dofs 3 Displacement
  Exec Solver = Always
  Stabilize = True
  Bubbles = False
  Lumped Mass Matrix = False
  Optimize Bandwidth = True
  Steady State Convergence Tolerance = 1.0e-5
  Nonlinear System Convergence Tolerance = 1.0e-7
  Nonlinear System Max Iterations = 20
  Nonlinear System Newton After Iterations = 3
  Nonlinear System Newton After Tolerance = 1.0e-3
  Nonlinear System Relaxation Factor = 1
  Linear System Solver = Iterative
  Linear System Iterative Method = BiCGStab
  Linear System Max Iterations = 500
  Linear System Convergence Tolerance = 1.0e-10
  BiCGstabl polynomial degree = 2
  Linear System Preconditioning = ILU0
  Linear System ILUT Tolerance = 1.0e-3
  Linear System Abort Not Converged = False
  Linear System Residual Output = 10
  Linear System Precondition Recompute = 1
End

Equation 1                                          # Setting the active solvers
  Name = "Equation 1"
  Plane Stress = True
  Plane Stress = True
  Calculate Stresses = True
  Active Solvers(1) = 1
End

Material 1                                          # Defining the material
  Name = "Steel (carbon - generic)"
  Heat Capacity = 1265.0
  Poisson ratio = 0.3
  Electric Conductivity = 1.449e6
  Electric Conductivity = 1.449e6
  Porosity Model = Always saturated
  Youngs modulus = 2.1e11
  Density = 7800.0
  Mesh Poisson ratio = 0.3
  Youngs modulus = 2.1e11
  Heat expansion Coefficient = 13.8e-6
  Heat Conductivity = 44.8
  Poisson ratio = 0.3
  Electric Conductivity = 1.449e6
  Youngs modulus = 2.1e11
  Sound speed = 5100.0
  Electric Conductivity = 1.449e6
  Electric Conductivity = 1.449e6
  Poisson ratio = 0.3
End

Boundary Condition 1                                # Applying the boundary conditions
  Target Boundaries(1) = 3
  Name = "AB"
  Displacement 1 = 0
End

Boundary Condition 2
  Target Boundaries(1) = 6
  Name = "CD"
  Displacement 2 = 0
End

Boundary Condition 3
  Target Boundaries(1) = 4
  Name = "BC"
  Displacement 2 = 0
  Displacement 1 = 0
End

Boundary Condition 4
  Target Boundaries(1) = 1
  Name = "LOAD"
  Normal Force = 1e6
End

Boundary Condition 5
  Target Boundaries(1) = 9
  Name = "EE"
  Displacement 3 = 0
End

```


The simulation input file used in this study can be found on our [GitHub](https://github.com/spolanski/CoFEA/tree/master/benchmarks/01-LE10-Thick-Plate/Model_ElmerGUI)!