# Eclipse project for examples

- Open Eclipse
- Click File --> New --> C/C++ Project
	1. Input Project name --> Uncheck use default location --> Provide the location of the example folder
    <figure markdown>
        ![Image: Eclipse C Project for Windows](eclipse_project_windows.jpg){ width="500"}
        <figcaption>Fig. 8: Eclipse C Project for Windows</figcaption>
    </figure>
    <figure markdown>
        ![Image: Eclipse C Project for Linux](eclipse_project_linux.jpg){ width="500"}
        <figcaption>Fig. 9: Eclipse C Project for Linux</figcaption>
    </figure>

	2. Select Executable --> Empty project in Project type		
	3. For Windows, Select MinGW GCC as Toolchain
	4. For Linux, Select Linux GCC as Toolchain		


- In Project Explorer window, Right click on the project created --> Click Properties --> C/C++ Build --> Tool Chain Editor --> Select Current builder as Gnu Make Builder
- Again click on C/C++ Build
	1. For Windows, Uncheck `"Use default build command"` and type build command as `mingw32-make`
	2. Uncheck generate Makefiles automatically 
	3. Ensure Build location path is chosen from the workspace
	<figure markdown>

        ![Image: Windows Eclipse Project Properties](eclipse_properties_windows.jpg){ width="700"}
        <figcaption>Fig. 10: Windows Eclipse Project Properties</figcaption>
    </figure>
    <figure markdown>

        ![Image: Linux Eclipse Project Properties](eclipse_properties_linux.jpg){ width="700"}
        <figcaption>Fig. 11: Linux Eclipse Project Properties</figcaption>
    </figure>
    
	4. Click Apply and Close button



## Build project

In Project Explorer window, Right click on the project --> Click Build Project. The executable file will be generated.

## Debug project

- Click on Run --> Debug As --> Local C/C++ Application
- Once launching is completed, Click on 
    1. Resume button to run the application
    2. Terminate button to stop running the application
<figure markdown>

  ![Image: Eclipse Debug Configuration](eclipse_debug_config.jpg){ width="700"}
  <figcaption>Fig. 12: Eclipse Debug Configuration</figcaption>
</figure>
