# unity_official_docs_incremental_260527

This file is a Dify upload bundle generated from local JSONL sources.


---

<!-- source=unity_docs; title=UI Toolkit project settings; url=https://docs.unity3d.com/6000.4/Documentation/Manual/UIB-project-setting.html -->

# UI Toolkit project settings

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/UIB-project-setting.html

Unity Editor interface
Unity Editor settings reference
Project Settings reference
UI Toolkit project settings
UI Toolkit project settings
To view the UI Toolkit project settings, go to
Edit
>
Project Settings
>
UI Toolkit
.
UI Builder
When you create a new UI Document (UXML) in the UI Builder, certain features are set by default:
The UI Document is set to suit runtime UI.
The UI Builder library only displays UI controls that are available for runtime UI.
You can easily zoom in and out of the canvas of the
Viewport
The user’s visible area of an app on their screen.
See in
Glossary
window in UI Builder using your mouse wheel or trackpad.
To ensure that newly created documents are, by default, compatible with Editor UI and that the UI Builder library displays the additional controls for Editor UI, select
Enable Editor Extension Authoring by Default
. For more information, refer to
Enable Editor Extension Authoring for UI Documents (UXML)
.
To disable zooming on your canvas using your mouse wheel or trackpad, select
Disable Viewport Zooming via Mouse Wheel/Trackpad
.
Advanced
The UI Toolkit Event Debugger is an experimental feature that helps you to discover how various UI Toolkit events, such as input, layout, and paint, are handled. The
UI Toolkit Event Debugger
window is disabled by default. To enable it, Select
Enable Event Debugger
. To access it once enabled, select
Windows
>
UI Toolkit
>
Event Debugger
.
The UI Toolkit Layout Debugger is an experimental feature that helps you to discover what styles and settings affect an element on the screen. The
UI Toolkit Layout Debugger
window is disabled by default. To enable it, Select
Enable Layout Debugger
. To access it once enabled, select
Windows
>
UI Toolkit
>
Layout Debugger
.
Additional resources
UI Toolkit
UI Builder
Control behavior with events


---

<!-- source=unity_docs; title=Managing time and frame rate; url=https://docs.unity3d.com/6000.4/Documentation/Manual/managing-time-and-frame-rate.html -->

# Managing time and frame rate

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/managing-time-and-frame-rate.html

Programming in Unity
Object-oriented development
Managing time and frame rate
Managing time and frame rate
It’s important to understand how Unity handles time to ensure your gameplay remains stable. Updates occur at regular time intervals to capture changes to character positions, health status, scores, and so on. If your code makes changes in the wrong update loop or doesn’t allow for variations in time, effects like movement might be too fast, too slow, or jumpy instead of smooth.
The
Time
class contains properties through which you can get and in some cases set various time-related measurements and settings. Refer to
Time
in the Scripting API reference for a complete list of the properties and their meanings.
Topic
Description
Per-frame updates
Updates which happen once per frame and whose frequency therefore depends on frame rate.
Fixed updates
Updates which happen at a configurable fixed time interval.
In-game time and real time
The configurable relationship between in-game time and real time and the potential effects.
Handling variation in time
Techniques Unity uses to compensate for variations in time and frame rate and to limit the effects of one-time delays.
Capture frame rate
Compensating for frame rate when recording video of gameplay.
Simulate hitches for testing
Simulate hitches to test how your game handles time variation caused by performance issues.
Additional resources
Time API reference
Time settings in the Editor


---

<!-- source=unity_docs; title=Unity - Manual: Fixed updates; url=https://docs.unity3d.com/6000.4/Documentation/Manual/fixed-updates.html -->

# Unity - Manual: Fixed updates

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/fixed-updates.html

Programming in Unity
Object-oriented development
Managing time and frame rate
Fixed updates
Fixed updates
Unlike the main
frame update
, Unity’s physics system updates at a fixed time interval, which is important for the accuracy and consistency of physics simulations. The interval between fixed updates is often referred to as the
fixed timestep
A customizable frame-rate-independent interval that dictates when physics calculations and FixedUpdate() events are performed.
More info
See in
Glossary
. You can read or change the fixed timestep in two ways:
In code, by setting the value of the
Time.fixedDeltaTime
property .
In the Unity Editor’s
Time
window, by modifying the
Fixed Timestep
value.
In both cases the fixed time step is specified in seconds. For example, a value of 0.01 means each fixed time step is one hundredth of a second in duration, so there are 100 fixed updates per second.
The fixed update loop simulates code running at fixed time intervals but in practice the interval between fixed updates isn’t fixed. This is because a fixed update always needs a frame to run in and the duration of a frame and the length of the fixed time step are not in perfect sync. If a fixed time step completes during the current frame, the associated fixed update can’t run until the next frame.
When frame rates are low
, a single frame might span several fixed time steps. In this case a backlog of fixed updates accumulates during the current frame and Unity executes all of them in the next frame to catch up.
Note:
There is a maximum timestep period beyond which Unity will not attempt to catch up with the simulation. For more information, refer to
Handling variation in time
.
Unity provides the
MonoBehaviour.FixedUpdate
method as an entry point for you to execute your own code on each fixed update. This is most commonly used for executing your own physics-related code, such as
applying a force
to a
Rigidbody
A component that allows a GameObject to be affected by simulated gravity and other forces.
More info
See in
Glossary
.
You can see more details of what occurs during the fixed update cycle in the
Physics
section of the
execution order diagram
diagram.
When frame rate is higher than the fixed update rate
If your application runs at a higher frame rate than the number of fixed time steps per second then the average frame duration is less than the duration of a single fixed time step. In this case, each frame has one fixed update or none at all. For example, if the fixed time step value is 0.02, there are 50 fixed updates per second. If your application runs at around 128
frames per second
The frequency at which consecutive frames are displayed in a running game.
More info
See in
Glossary
, a fixed update occurs every two or three frames, as shown below.
![An example showing FixedUpdate running at 50 updates per second (0.02s per fixed update) and the Player Loop running at approximately 128 frames per second. Some frame updates (marked in yellow) have a corresponding FixedUpdate (marked in green) if a new complete fixed timestep has elapsed by the start of the frame.](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/TimingFixedUpdateFastFPS.png)
An example showing FixedUpdate running at 50 updates per second (0.02s per fixed update) and the Player Loop running at approximately 128 frames per second. Some frame updates (marked in yellow) have a corresponding FixedUpdate (marked in green) if a new complete fixed timestep has elapsed by the start of the frame.
This diagram shows the frame rate running faster than the fixed update timestep rate. Time progresses to the right, each frame is numbered, and shows its
Update
call at the start of the frame in orange. The fixed timestep here is 0.02 seconds (50 times per second), and the game is running faster, at about 128 frames per second. In this situation there are some frames with one fixed update call, and some frames with none, depending on whether a full fixed update timestep has completed by the time the frame starts. The fixed time step periods are marked with letters A, B, C, D, E, and the frames in which their corresponding fixed update calls occur are marked in green. The fixed update call for timestep A occurs at the start of frame 4, the fixed update call for timestep B occurs at the start of frame 7, and so on.
When frame rate is lower than the fixed update rate
If your application runs at a lower frame rate than the fixed timestep value then the average frame duration is longer than a single fixed timestep. This means a backlog of fixed updates can accumulate during some frames and so each frame has one or more fixed updates to allow the physics simulation to catch up with the backlog. For example, if the fixed timestep value is 0.01, there are 100 fixed updates per second. If your application runs at around 40 frames per second, Unity performs an average of two or three fixed updates per frame to keep up. You might want a scenario like this when it’s more important to model more accurate physics than to have a high frame rate.
![An example showing Update running at around 38 FPS and FixedUpdate running at 100 updates per second. As a result, some frames have up to three FixedUpdates (marked in green).](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/TimingFixedUpdateSlowFPS.png)
An example showing Update running at around 38 FPS and FixedUpdate running at 100 updates per second. As a result, some frames have up to three FixedUpdates (marked in green).
This diagram shows what happens when the fixed update cycle is running faster than the frame rate. The fixed timestep here is 0.01 seconds (100 times per second), and the game frame rate is running slower, at about 38 frames per second. In this situation most frames have multiple fixed update calls before each update call, the number depending on how many whole update timesteps have elapsed since the previous frame. The fixed update time step periods are marked with letters A, B, C, and so on, and frames in which their corresponding fixed update calls occur are marked in green. The fixed update call for timestep A and B occurs at the start of frame 2, the fixed update call for frames C, D & E occur at the start of frame 3, and so on.
Note:
A lower timestep value means more frequent physics updates and more precise simulations, which leads to higher CPU load.
Additional resources
Managing variable frame rate
Handling variations in time
Time scale
Capture frame rate


---

<!-- source=unity_docs; title=Optimize physics performance; url=https://docs.unity3d.com/6000.4/Documentation/Manual/physics-optimization.html -->

# Optimize physics performance

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/physics-optimization.html

Physics
Built-in 3D physics
Optimize physics performance
Optimize physics performance
Optimize physics system performance in the Unity Editor.
Use the guidance in these pages to optimize the physics system so you can maintain your target frame rate and ensure smooth, responsive gameplay. The instructions in these pages address issues identified by Unity Editor diagnostic tools. Before you apply the optimizations described in the documentation in this section and throughout your development, you must be familiar with these diagnostic tools:
The Unity Profiler
: The Profiler is the primary tool to measure CPU performance. The Profiler helps identify bottlenecks in your project, particularly in areas such as
Physics.FixedUpdate
and
Physics.Simulate
, and in its detailed breakdowns of physics phases such as broad phase and narrow phase processing. To open the Profiler window, go to
Window > Analysis > Profiler
.
The Memory Profiler
: Use the Memory Profiler to identify and optimize memory allocations caused by physics operations, such as excessive
RaycastHit
arrays or frequent
collision
A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion.
More info
See in
Glossary
data creation. You can use this information to reduce your garbage collection overhead.
The Physics Debug
window: Use this tool to visually diagnose physics-related performance issues. It displays collision shapes, contacts, broad phase bounding boxes, and Rigidbody component sleep states. This helps you identify areas like overly complex colliders, unnecessary interactions, or objects failing to sleep, all of which contribute to performance bottlenecks. To open the Physics Debug window, select
Window > Analysis > Physics Debug
.
Topic
Description
Optimize the physics system for CPU usage
Optimize Unity’s physics system’s CPU usage by adjusting simulation frequency, managing
colliders
An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay.
More info
See in
Glossary
, and configuring
Rigidbody
A component that allows a GameObject to be affected by simulated gravity and other forces.
More info
See in
Glossary
components.
Optimize the physics system for memory usage
Optimize Unity’s physics system’s memory usage by controlling collision callbacks and optimizing physics queries.
Understand physics performance issues
Understand performance issues related to physics in your application.
Additional resources
Unity Profiler
Built-in 3D Physics
Memory Profiler
Physics Project Settings


---

<!-- source=unity_docs; title=Overlays; url=https://docs.unity3d.com/6000.4/Documentation/Manual/overlays.html -->

# Overlays

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/overlays.html

Scenes
Manage GameObjects in the Scene view
Overlays
Overlays
You can access authoring tools in the
Scene
A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces.
More info
See in
Glossary
view as customizable panels and
toolbars
A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation).
More info
See in
Glossary
called overlays. Overlays can also display contextual information about your selection. Any package you install can add an overlay to your scene. To choose which overlays appear in your scene, refer to
Overlays menu reference
.
To improve your workflow you can position overlays, select which overlays to display or hide, and save, import, or export overlay configurations.
‍To check which overlays are available in the
Scene view
An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object.
More info
See in
Glossary
, press the
`
key to open the Overlay menu. You can also open the Overlay menu from the
More
(⋮) menu in the top right corner of the Scene view.
Topic
Description
Overlays reference
Learn about the settings and operations of different overlays in the Scene view.
Change the appearance and position of an overlay
Change the visibility, shape, and location of an overlay in the Scene view.
Create and manage overlay presets
Save, switch, import, and export overlay configurations.
Cameras overlay
Manage cameras in the Scene view and take first-person control of
GameObjects
The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it.
More info
See in
Glossary
that have
camera
A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture.
More info
See in
Glossary
components attached to them.
Orientation overlay
Change the Scene camera’s orientation, viewing angle and projection mode.
Additional resources
Position GameObjects
Create custom Editor tools


---

<!-- source=unity_docs; title=Per-pixel and per-vertex lights in the Built-In Render Pipeline; url=https://docs.unity3d.com/6000.4/Documentation/Manual/PerPixelLights-BuiltIn.html -->

# Per-pixel and per-vertex lights in the Built-In Render Pipeline

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/PerPixelLights-BuiltIn.html

Lighting
Lighting in the Built-In Render Pipeline
Per-pixel and per-vertex lights in the Built-In Render Pipeline
Per-pixel and per-vertex lights in the Built-In Render Pipeline
If you use the default
Forward rendering path
, Unity sets each realtime Light component as one of the following types:
Per-pixel light
Per-vertex light
Spherical harmonics (SH) per-vertex light
For more information, refer to
Per-pixel and per-vertex lights
.
The Built-In
Render Pipeline
A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own.
More info
See in
Glossary
renders each
GameObject
The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it.
More info
See in
Glossary
once for each per-pixel light that affects it.
SH lights are fast, and have little or no performance impact. However, SH lights don’t support cookies,
normal maps
A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.
See in
Glossary
, or specular highlights. They also have sharp lighting transitions, and might look incorrect.
How Unity classifies lights
By default, Unity groups lights using the following criteria:
The brightest light is always a per-pixel light. This is usually the main Directional Light.
The 4 next most important lights are per-vertex lights.
The remaining lights are SH lights.
During rendering, Unity finds all lights surrounding a
mesh
The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
More info
See in
Glossary
and calculates which of those lights affect it most.
For example, in the following image where a sphere GameObject is lit by 8 lights with the same color and intensity, Unity sets the four closest lights (A to D) as per-pixel lights, lights D to G to per-vertex lights, and lights G and H as SH lights. Each per-pixel light creates a separate render pass.
![A sphere GameObject lit by 8 lights](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/ForwardLightsExample.png)
A sphere GameObject lit by 8 lights
![How Unity classifies the lights](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/ForwardLightsClassify.png)
How Unity classifies the lights
To help avoid visible light transitions when GameObjects and lights move, Unity blends lights from one mode to another. In the preceding example, Unity blends light D from a per-pixel light to a per-vertex light.
For information about optimizing how Unity classifies lights, refer to
Optimize lighting in the Built-In Render Pipeline
.
Additional resources
Per-pixel and per-vertex lights


---

<!-- source=unity_docs; title=Frame Debugger Event Information reference; url=https://docs.unity3d.com/6000.4/Documentation/Manual/frame-debugger-window-event-information.html -->

# Frame Debugger Event Information reference

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/frame-debugger-window-event-information.html

Optimization
Graphics performance and profiling
Graphics performance and profiling reference
Frame Debugger Event Information reference
Frame Debugger Event Information reference
The Event Information Panel in the
Frame Debugger window
displays information about the event such as geometry details and the
shader
A program that runs on the GPU.
More info
See in
Glossary
used for a draw call.
![The Event Information Panel showing the URP sample scene. The top bar has selectors for the render target, color channels, and levels (A, B, and C). The central area is the mesh preview (D). The bottom area lists event properties (E).](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/frame-debugger-window-event-information.png)
The Event Information Panel showing the URP sample scene. The top bar has selectors for the render target, color channels, and levels (A, B, and C). The central area is the mesh preview (D). The bottom area lists event properties (E).
Label
Description
A
Render target selector
: When rendering into multiple render targets (such as multiple
RenderTextures
or when also rendering to depth), this specifies which render target to display in the Game view. This is useful for example to view individual render targets in a G-buffer.
B
Color channel selector
: Specifies which color channels of the render target to display.
C
Levels
: Controls the black and white intensity. Use this to isolate areas of the Game view based on light intensity.
D
Output /
Mesh
The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
More info
See in
Glossary
Preview
: Displays a preview of the selected event output as well as the mesh geometry in the event. For more information, see
Preview
.
E
Event properties
: Contains further information about the selected event. For more information, see
Event properties
.
Preview
The preview section consists of two tabs:
The
Output
tab displays a preview of the selected event output.
The
Mesh Preview
tab displays the mesh geometry Unity rendered in the event.
![The mesh preview tab displaying the power jigsaw mesh from the URP sample scene. The mesh preview (A) is in the centre. The bottom bar has the mesh name (B), the preview mode (C), and the toggle for wireframe (D).](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/frame-debugger-mesh-preview.png)
The mesh preview tab displaying the power jigsaw mesh from the URP sample scene. The mesh preview (A) is in the centre. The bottom bar has the mesh name (B), the preview mode (C), and the toggle for wireframe (D).
Label
Description
A
Preview
: A preview of the mesh geometry Unity rendered during the event.
B
Mesh name
: The name of the mesh asset in the preview. Click on the mesh name to take see the mesh asset in the
Project window
A window that shows the contents of your
Assets
folder (Project tab)
More info
See in
Glossary
. If the geometry was procedural and there is no mesh asset associated, this is empty (Unity displays
-
).
C
Preview mode
: Specifies how the preview renders the mesh. For more information, refer to
Preview mode dropdown
.
D
Wireframe toggle
: Toggles the mesh wireframe on and off. When enabled, the preview displays the mesh vertices and edges.
Preview mode dropdown
Value
Description
Shaded
Renders the mesh using its material and a basic light.
UV Checker
Applies a checkerboard texture to the mesh to visualize how the mesh’s UV layout maps textures.
UV Layout
Displays how the vertices of the mesh are organized in the unwrapped UV layout. This view disables the Wireframe toggle.
Vertex Color
Visualizes any vertex colors that the vertices in this mesh have. If no vertices have a vertex color, this option is unavailable.
Normals
Visualizes the relative directions of the normals in the mesh with color.
Tangents
Visualizes the tangent data in the mesh with color.
Blendshapes
Visualizes blend shape deformations on the mesh. If the mesh has no blend shapes, this option is unavailable.
Event properties
The event properties section contains properties and values for the selected event. It has a
Details
fold-out section that contains information about the event itself and then a fold-out section for each type of shader property. If the fold-out section is grayed-out, it means that the shader in the event didn’t contain any properties of that type. For more information on the information that each section displays, see:
Details
Keywords
Textures
An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail.
More info
See in
Glossary
Ints
Floats
Vectors
Matrices
Buffers
Constant Buffers
Note
: When using OpenGL and GLSL shaders, this panel displays all shader properties as being part of the vertex stage.
Details
The
Details
section displays information about the rendering event, such as the number of draw calls as well as the meshes that Unity rendered and the shader it used to render them.
Property
Description
RenderTarget
Defines the name of the render target.
Size
Specifies the size of the render target.
Format
Defines the
TextureFormat
for the render target.
Color Actions
Displays the actions Unity performs on the color target when:
The GPU first loads the color target. For more information, refer to
RenderBufferLoadAction
.
The GPU finishes rendering to the color target. For more information, refer to
RenderBufferStoreAction
.
Depth Actions
Displays the actions Unity performs on the depth target when:
The GPU first loads the depth target. For more information, refer to
RenderBufferLoadAction
.
The GPU finishes rendering to the depth target. For more information, refer to
RenderBufferStoreAction
.
Memoryless
Specifies the
render texture
A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture.
More info
See in
Glossary
memoryless mode
mode. For more information, refer to
memoryless
.
ColorMask
Defines the color channel mask Unity uses for the render target. For more information, refer to
ColorMask
.
Blend Color
Specifies the
color blending
method Unity uses during the selected event.
Blend Alpha
Specifies the
alpha blending
method Unity uses during the selected event.
BlendOp Color
Defines the
color blending operation
Blend Color Unity uses.
BlendOp Alpha
Defines the
alpha blending operation
Blend Alpha Unity uses.
Draw Calls
Displays the number of draw calls Unity processes during the selected event.
Vertices
Displays the number of vertices Unity processes during the selected event.
Indices
Displays the number of indices Unity processes during the selected event.
Clear Color
Specifies the color Unity uses to clear the render target during the selected event. If Unity doesn’t clear the render target, the display doesn’t show a color.
Clear Depth
Specifies the color Unity uses to clear the
depth buffer
A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane.
More info
See in
Glossary
during the selected event. If Unity doesn’t clear the depth buffer, the display doesn’t show a color.
Clear Stencil
Specifies the color Unity uses to clear the
stencil buffer
A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation.
More info
See in
Glossary
during the selected event. If Unity doesn’t clear the stencil buffer, the display doesn’t show a color.
Batch cause
Displays the reason why the SRP Batcher is unable to batch the selected rendering event with the previous rendering event.
Relevant only if your application uses the
SRP Batcher
.
Meshes
Displays the list of meshes that Unity renders during the selected event.
Pass
Defines the
shader Pass
Unity uses.
LightMode
Specifies the LightMode
pass tag
Unity uses during the selected event.
Base Shading Rate
Displays the
shading rate fragment size
Unity uses in the pass. Available only if the current platform supports variable rate shading.
ShadingRateCombiners
Displays the
shading rate combiners
Unity uses in the Primitive / Fragment stages. This is available only if a shading rate image is attached to the pass.
Shading Rate Image
Displays the
shading rate image
attachment Unity uses in the pass.
Used Shader
Specifies the
shader asset
Unity uses during the selected event. This can sometimes be different than the original shader, for example when the original shader uses a
fallback shader
or
USEPASS
.
Original Shader
Displays the original shader Unity uses with the pass.
ZClip
Specifies the shader’s
depth clip
mode.
ZTest
Specifies the shader’s
depth test
mode.
ZWrite
Specifies the shader’s
depth clip
mode.
Cull
Defines the shader’s
cull
mode.
Conservative
Indicates whether the shader uses
conservative rasterization
.
Offset
Specifies the
depth bias
on the GPU that Unity uses during the selected event.
Stencil
Indicates whether Stencil is enabled in the selected event. For more information, refer to
Stencil
.
Stencil Ref
Specifies the stencil reference value.
Stencil ReadMask
Defines the stencil
readmask
value Unity uses to perform the stencil test.
Stencil WriteMask
Defines the stencil
writemask
value Unity uses to write to the stencil buffer.
Stencil Comp
Specifies the operation the GPU performs for the stencil test for all
pixels
The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel.
More info
See in
Glossary
.
Stencil Pass
Specifies the operation the GPU performs on the stencil buffer for pixels that pass both the stencil test and the depth test.
Stencil Fail
Specifies the operation the GPU performs on the stencil buffer for pixels that fail the stencil test.
Stencil ZFail
Specifies the operation the GPU performs on the stencil buffer for pixels that pass the stencil test but fail the depth test.
Keywords
This section displays information about the enabled
shader keywords
Unity used in the rendering event.
Property
Description
Name
The name of the shader keyword.
Stage
The shader stage that Unity used the shader keyword in. Refer to
Stages
.
Scope
Indicates whether the scope of the keyword is global or local. For more information, refer to
Toggle shader keywords in a script
.
Dynamic
Indicates whether the keyword is dynamic or not. For more information, see
Declaring and using shader keywords in HLSL
.
Textures
The
Texture
section displays information about the named
textures
Unity used during the rendering event.
Property
Description
Name
The property name for the texture.
Stage
The shader stage that Unity used the texture in. Refer to
Stages
.
Size
The size of the texture. This is the width and height for 2D textures and width, height, and depth for 3D textures,
Sampler Type
Indicates type of a Texture (such as 2D Texture, cubemap, or 3D volume texture).
Color Format
The color format that the texture uses. For more information on RenderTexture formats, see
GraphicsFormat
. For more information on formats for other texture types, see
TextureFormat
.
Depth Stencil Format
The depth stencil format for the RenderTexture. For more information, see
RenderTexture.depthStencilFormat
.
Note
: If the texture isn’t a RenderTexture, Unity doesn’t display a
graphics format
here.
Texture
The texture name.
Ints
The
Ints
section displays information about the named
int
values Unity used during the rendering event.
Property
Description
Name
The name of the int property in the shader.
Stage
The shader stage that Unity used the int property in. Refer to
Stages
.
Value
The value of the int property.
Floats
The
Floats
section displays information about the named
float
values Unity used during the rendering event.
Property
Description
Name
The name of the float property in the shader.
Stage
The shader stage that Unity used the float property in. Refer to
Stages
.
Value
The value of the float property.
Vectors
Property
Description
Name
The name of the vector property in the shader.
Stage
The shader stage that Unity used the vector property in. Refer to
Stages
.
Value(R)
The R component of the vector.
Value(G)
The G component of the vector.
Value(B)
The B component of the vector.
Value(A)
The A component of the vector.
Matrices
The
Matrices
section displays information about the named
matrix
values Unity used during the rendering event.
Property
Description
Name
The name of the matrix property in the shader.
Stage
The shader stage that Unity used the matrix property in. Refer to
Stages
.
Column 0
The values in the first column of the matrix.
Column 1
The values in the second column of the matrix.
Column 2
The values in the third column of the matrix.
Column 3
The values in the fourth column of the matrix.
Buffers
The
Buffers
section displays information about the named
buffers
Unity used during the rendering event.
Property
Description
Name
The name of the buffer in the shader.
Stage
The shader stage that Unity used the buffer in. Refer to
Stages
.
Constant Buffers
This
Constant Buffers
section displays information about the named
constant buffers
Unity used during the rendering event.
Property
Description
Name
The name of the constant buffer in the shader.
Stage
The shader stage that Unity used the constant buffer in. Refer to
Stages
.
Stages
The possible values for
Stage
are:
vs
: Vertex Shader
fs
: Fragment Shader
gs
: Geometry Shader
hs
: Hull Shader
ds
: Domain Shader


---

<!-- source=unity_docs; title=RenderDoc integration; url=https://docs.unity3d.com/6000.4/Documentation/Manual/RenderDocIntegration.html -->

# RenderDoc integration

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/RenderDocIntegration.html

Optimization
Graphics performance and profiling
Graphics performance and profiling reference
RenderDoc integration
RenderDoc integration
The Editor supports integrated launching and capture of the
RenderDoc
graphics debugger, for detailed frame introspection and debugging.
The integration is only supported for RenderDoc versions 0.26 or later, so if an earlier version is currently installed it is required that you update to at least version 0.26.
Note:
While the integration is only available in the Editor, it is quite possible to use RenderDoc as normal with no extra setup in standalone player builds.
Note:
Frames can only be captured if Unity is running on a platform and API that RenderDoc supports. If another API is in use, the RenderDoc integration will be temporarily disabled until a supported API is enabled. Refer to the
RenderDoc documentation
for more information on supported platforms and APIs.
Loading RenderDoc
If a RenderDoc installation is detected, then at any time after loading the Editor you can right click on the tab for the
Game View
or
Scene View
An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object.
More info
See in
Glossary
and click the ‘Load RenderDoc’ option. This will reload the graphics device so you must save any changes, but afterwards RenderDoc will be ready to capture without having to restart the editor or build a standalone player.
Note:
You can also launch the Editor via RenderDoc as normal, or pass the -load-renderdoc command line option to load RenderDoc from startup.
Capturing a frame with RenderDoc
When a compatible version of RenderDoc is detected as loaded into the Editor, a new button will appear on the right side of the
toolbar
A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation).
More info
See in
Glossary
on the Game and
Scene
A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces.
More info
See in
Glossary
Views.
![Capturing a frame with RenderDoc](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/RenderDocCaptureButton.png)
Capturing a frame with RenderDoc
Pressing this button will trigger a capture of the next frame of rendering for the view. If the RenderDoc tool UI has not been opened, a new instance will be launched to show the capture, and if it is already running the newest capture will automatically appear there. From there you can open the capture and debug using the tool.
![List of frame captures in RenderDoc](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/RenderDocCaptureList.jpg)
List of frame captures in RenderDoc
Including shader debug information
By default to optimise the size of DirectX11 shaders, debugging information is stripped out. This means that constants and resources will have no names, and the
shader
A program that runs on the GPU.
More info
See in
Glossary
source will not be available. To include this debugging information in your shader, include
#pragma enable_d3d11_debug_symbols
in your shader’s
HLSLPROGRAM
block.
Alternative graphics debugging techniques
If you build a standalone player using D3D11, you can capture a frame and debug using the
Visual Studio graphics debugger
.
Configuring Android SDK in RenderDoc
When using RenderDoc to develop Android applications, ensure to configure the Android SDK correctly using one of the following ways:
Set RenderDoc to use the same SDK as Unity (recommended)
In the RenderDoc window, go to
Tools
>
Settings
>
Android
.
Under
Android SDK root path
, enter the path that Unity uses for Android SDK. You can find this path in the Unity Editor under
Edit
>
Preferences
>
Android SDK Tools Installed with Unity
.
Align ADB versions and paths between RenderDoc and Unity
If the
Android SDK root path
in RenderDoc settings isn’t set, RenderDoc uses the path set for
ADB
An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building.
More info
See in
Glossary
in the
PATH
environment variable.
Find the ADB path set in the
PATH
variable.
Windows PowerShell:
Get-Command adb | Select-Object Path
Windows command prompt:
where adb
Check the ADB version in Windows terminal:
C:\[adb path from command output]\adb.exe version
.
Find the ADB path that Unity uses. In the Unity Editor, go to
Edit
>
Preferences
>
Android SDK Tools Installed with Unity
.
Check the corresponding ADB version in Windows terminal:
C:\[path to Android sdk platform-tools]\adb.exe version
.
Compare the ADB versions that RenderDoc and Unity use. If they differ, choose one of the ADB locations and configure both tools to use the same path.
Note
: Make sure platform-tools from the selected SDK are
up to date
by using the Android SDK manager in Android Studio.


---

<!-- source=unity_docs; title=Mesh .triangles; url=https://docs.unity3d.com/6000.4/Documentation/ScriptReference/Mesh-triangles.html -->

# Mesh .triangles

- Source: unity_docs
- Section: ScriptReference
- URL: https://docs.unity3d.com/6000.4/Documentation/ScriptReference/Mesh-triangles.html

Mesh
.triangles
Switch to Manual
public int[]
triangles
;
Description
An array containing all triangles in the Mesh.
The array is a list of triangles that contains indices into the vertex array. The size of the triangle array must always be a multiple of 3.
Vertices can be shared by simply indexing into the same vertex.
If the Mesh contains multiple sub-meshes (Materials), the triangle list will contain all the triangles belonging to all its sub-meshes.
When you assign a triangle array using this function, the
subMeshCount
is set to 1. If you want to have multiple sub-meshes, use
subMeshCount
and
SetTriangles
.
It is recommended to assign a triangle array after assigning the vertex array, in order to avoid out of bounds errors.
```csharp
// Builds a
Mesh
containing a single triangle with uvs.
// Create arrays of vertices, uvs and triangles, and copy them into the mesh.
using UnityEngine;
public class meshTriangles :
MonoBehaviour
{
// Use this for initialization
void Start()
{
gameObject.AddComponent<
MeshFilter
>();
gameObject.AddComponent<
MeshRenderer
>();
Mesh
mesh = GetComponent<
MeshFilter
>().mesh;
mesh.Clear();
// make changes to the
Mesh
by creating arrays which contain the new values
mesh.vertices = new
Vector3
[] {new
Vector3
(0, 0, 0), new
Vector3
(0, 1, 0), new
Vector3
(1, 1, 0)};
mesh.uv = new
Vector2
[] {new
Vector2
(0, 0), new
Vector2
(0, 1), new
Vector2
(1, 1)};
mesh.triangles = new int[] {0, 1, 2};
}
}
```
Additional resources:
SetTriangles
,
SetIndices
.


---

<!-- source=unity_docs; title=Mesh .vertices; url=https://docs.unity3d.com/6000.4/Documentation/ScriptReference/Mesh-vertices.html -->

# Mesh .vertices

- Source: unity_docs
- Section: ScriptReference
- URL: https://docs.unity3d.com/6000.4/Documentation/ScriptReference/Mesh-vertices.html

Mesh
.vertices
Switch to Manual
public Vector3[]
vertices
;
Description
Returns a copy of the vertex positions or assigns a new vertex positions array.
The number of vertices in the Mesh is changed by assigning a vertex array with a different number of vertices.
If you resize the vertex array then all other vertex attributes (normals, colors, tangents, UVs) are automatically resized too.
RecalculateBounds
is automatically invoked if no vertices have been assigned to the Mesh when setting the vertices.
Note that this method returns the vertices in local space, not in world space.
```csharp
using UnityEngine;
public class Example :
MonoBehaviour
{
Mesh
mesh;
Vector3
[] vertices;
void Start()
{
mesh = GetComponent<
MeshFilter
>().mesh;
vertices = mesh.vertices;
}
void
Update
()
{
for (var i = 0; i < vertices.Length; i++)
{
vertices[i] +=
Vector3.up
Time.deltaTime
;
}
// assign the local vertices array into the vertices array of the
Mesh
.
mesh.vertices = vertices;
mesh.RecalculateBounds();
}
}
```
Note:
To make changes to the
vertices
it is important to
copy the vertices from the
Mesh
. Once the
vertices
have been copied and
changed the
vertices
can be reassigned back to the
Mesh
.


---

<!-- source=unity_docs; title=Scriptable Render Pipeline Batcher in URP; url=https://docs.unity3d.com/6000.4/Documentation/Manual/SRPBatcher.html -->

# Scriptable Render Pipeline Batcher in URP

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/SRPBatcher.html

Optimization
Graphics performance and profiling
Graphics performance and profiling in URP
Optimizing draw calls in URP
Scriptable Render Pipeline (SRP) Batcher in URP
Scriptable Render Pipeline Batcher in URP
Scriptable Render Pipeline Batcher in URP
The Scriptable
Render Pipeline
A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own.
More info
See in
Glossary
(SRP) Batcher is a
draw call optimization
that significantly improves performance for applications that use an SRP. The SRP Batcher reduces the CPU time Unity requires to prepare and dispatch draw calls for materials that use the same
shader
A program that runs on the GPU.
More info
See in
Glossary
variant.
![The Scriptable Render Pipeline (SRP) Batcher reduces the CPU time Unity requires to render scenes with many materials that use the same shader variant.](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/SRPBatcher.png)
The Scriptable Render Pipeline (SRP) Batcher reduces the CPU time Unity requires to render scenes with many materials that use the same shader variant.
Requirements and compatibility
This section includes information about the render pipeline compatibility of the SRP Batcher.
Render pipeline compatibility
Feature
Universal Render Pipeline (URP)
High Definition Render Pipeline (HDRP)
Custom Scriptable Render Pipeline (SRP)
Built-in Render Pipeline
SRP Batcher
Yes
Yes
Yes
No
How the SRP Batcher works
The traditional way to optimize draw calls is to reduce the number of them. Instead, the SRP Batcher reduces render-state changes between draw calls. To do this, the SRP Batcher combines a sequence of
bind
and
draw
GPU commands. Each sequence of commands is called an SRP batch.
![The batching of bind and draw commands reduces the GPU setup between draw calls.](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/SROShaderPass.png)
The batching of bind and draw commands reduces the GPU setup between draw calls.
To achieve optimal performance for your rendering, each SRP batch should contain as many
bind
and
draw
commands as possible. To achieve this, use as few shader variants as possible. You can still use as many different materials with the same shader as you want.
When Unity detects a new material during the render loop, the CPU collects all properties and binds them to the GPU in constant buffers. The number of GPU buffers depends on how the shader declares its constant buffers.
The SRP Batcher is a low-level render loop that makes material data persist in GPU memory. If the material content doesn’t change, theSRP Batcher doesn’t make any render-state changes. Instead, the SRP Batcher uses a dedicated code path to update the Unity Engine properties in a large GPU buffer, like this:
![The SRP Batcher rendering workflow. The SRP Batcher uses a dedicated code path to update the Unity Engine properties in a large GPU buffer.](https://docs.unity3d.com/6000.4/Documentation/uploads/Main/SRP_Batcher_loop.png)
The SRP Batcher rendering workflow. The SRP Batcher uses a dedicated code path to update the Unity Engine properties in a large GPU buffer.
Here, the CPU only handles the Unity Engine properties, labeled
Per Object large buffer
in the above diagram. All materials have persistent constant buffers located in GPU memory, which are ready to use. This speeds up rendering because:
All material content now persists in GPU memory.
Dedicated code manages a large per-object GPU constant buffer for all per-object properties.


---

<!-- source=unity_docs; title=Enable the GPU Resident Drawer in URP; url=https://docs.unity3d.com/6000.4/Documentation/Manual/urp/gpu-resident-drawer.html -->

# Enable the GPU Resident Drawer in URP

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/urp/gpu-resident-drawer.html

Optimization
Graphics performance and profiling
Graphics performance and profiling in URP
Optimizing draw calls in URP
GPU Resident Drawer
Enable the GPU Resident Drawer in URP
Enable the GPU Resident Drawer in URP
The GPU Resident Drawer automatically uses the
BatchRendererGroup
API to draw
GameObjects
The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it.
More info
See in
Glossary
with GPU instancing, which reduces the number of draw calls and frees CPU processing time. For more information, refer to
How BatchRendererGroup works
.
The GPU Resident Drawer works only with the following:
A
Render Pipeline
A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own.
More info
See in
Glossary
Asset containing only Renderers using the
Forward+
or
Deferred+
rendering paths
The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others.
More info
See in
Glossary
.
Graphics APIs
and platforms that support compute
shaders
A program that runs on the GPU.
More info
See in
Glossary
, except OpenGL ES and VisionOS.
Realtime Global Illumination with Enlighten
disabled.
GameObjects that have a
Mesh Renderer component
which:
Does not use the
Use Proxy Volume
nor set the
Anchor Override
property in their
Light Probes
Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space.
More info
See in
Glossary
setting.
Does not have
MaterialPropertyBlocks
set on them.
Has default values for their
sortingLayerID
or
sortingOrder
properties.
Uses materials which support
BatchRendererGroup
.
Uses no more than 128 materials.
GameObjects that do not have a
Text Mesh component
.
GameObjects that do not have
MonoBehaviour components
which implement either the
OnWillRenderObject, OnBecameVisible or OnBecameInvisible
event callbacks.
GameObjects that are in the hierarchy of
Animation or Animator
components.
Otherwise, Unity falls back to drawing the GameObject without GPU Resident Drawer.
If you enable the GPU Resident Drawer, the following applies:
Build times are longer because Unity compiles all the
BatchRendererGroup
shader variants into your build.
The
Probe Atlas Blending
is used by default when both the
Forward+
or
Deferred+
rendering paths and the GPU Resident Drawer are used.
Enable the GPU Resident Drawer
Follow these steps:
Go to
Project Settings
>
Graphics
, then in the
Shader Stripping
section set
BatchRendererGroup Variants
to
Keep All
.
Go to the active
URP Asset
and check
SRP Batcher
is enabled. If the property isn’t visible in the URP Asset, open the
More
(
⋮
) menu and select
Show All Advanced Properties
.
Set
GPU Resident Drawer
to
Instanced Drawing
.
Double-click the renderer in the
Renderer List
to open the Universal Renderer, then set
Rendering Path
to
Forward+
.
If you change or create GameObjects each frame, the GPU Resident Drawer updates with the changes.
To include or exclude GameObjects from the GPU Resident Drawer, refer to
Make a GameObject compatible with the GPU Resident Drawer
.
Unsupported features with GPU Resident Drawer
The following features are not supported when using GPU Resident Drawer:
LOD
The
Level Of Detail
(LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases.
More info
See in
Glossary
Group
animated cross-fading
: Animated cross-fading transitions are not supported. LOD transitions fall back to static, distance-based cross-fading.
Light shadow matrix override: Using
Light.shadowMatrixOverride
in
scripts
A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like.
More info
See in
Glossary
doesn’t affect shadow caster culling.
Note:
The GPU Resident Drawer uses its own GPU
Occlusion culling
A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera.
More info
See in
Glossary
system, but supports
Dynamic Occlusion
as well.
Additional resources
Reduce rendering work on the CPU
Graphics performance fundamentals
GPU Resident Drawer performance considerations
GPU occlusion culling


---

<!-- source=unity_docs; title=Introduction to GPU instancing; url=https://docs.unity3d.com/6000.4/Documentation/Manual/GPUInstancing.html -->

# Introduction to GPU instancing

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/GPUInstancing.html

Optimization
Graphics performance and profiling
Optimize rendering lots of objects
GPU instancing
Introduction to GPU instancing
Introduction to GPU instancing
GPU instancing is a
draw call optimization
method that uses a single draw call to render multiple
GameObjects
The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it.
More info
See in
Glossary
that use the same
mesh
The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
More info
See in
Glossary
and material. This speeds up rendering when you draw things that appear multiple times in a
scene
A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces.
More info
See in
Glossary
, for example, trees or bushes.
GPU instancing is a built-in functionality of GPUs. Each copy of the mesh is called an instance. Each instance can have different properties, such as color or scale.
The performance benefits of GPU instancing depend on the platform and the GPU. For each draw call, Unity has to collect, combine, and upload properties from various memory locations, so the performance overhead might outweigh the benefits. The performance benefits are better on mobile platforms than on desktop platforms.
Render pipeline compatibility
GPU instancing is compatible with all Unity
render pipelines
A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own.
More info
See in
Glossary
, with the following limitations:
If you use the Universal Render Pipeline (URP) or High Definition Render Pipeline (HDRP), GPU instancing works with custom
shaders
A program that runs on the GPU.
More info
See in
Glossary
only if you disable the
Scriptable Render Pipeline (SRP) Batcher
or
make a shader incompatible with the SRP Batcher
.
If you use the Built-in Render Pipeline (BiRP), GPU Instancing doesn’t work with Shader Graph shaders.
For information on draw call optimization methods you can use instead of GPU instancing, refer to
Choose a method for optimizing draw calls
.
Indirect lighting compatibility
GPU instancing supports the following types of GameObject:
Dynamic GameObjects that get lighting from
Light Probes
Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space.
More info
See in
Glossary
.
Static GameObjects that get lighting from
lightmaps
A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting.
More info
See in
Glossary
, if they have
Contribute GI
enabled in their
Static Editor Flags
, and they bake to the same lightmap texture.
GameObjects that use
Light Probe Proxy Volumes
A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes).
More info
See in
Glossary
(LPPV). You must bake the LPPV for the entire space that contains all the instances.
Shader and mesh compatibility
The following meshes are compatible if you use prebuilt materials:
Mesh Renderer components
in your scene. Skinned
Mesh Renderer
A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component.
More info
See in
Glossary
components are not supported.
Meshes you render in a script using APIs that support GPU instancing in prebuilt materials, such as
Graphics.RenderMeshInstanced
.
The following shaders support GPU instancing:
Most
prebuilt materials
. Compatible shaders have an
Enable GPU Instancing
property.
Shader Graph
materials, if you use URP or HDRP.
To create a custom shader that supports GPU instancing, refer to the following:
Creating custom shaders that support GPU instancing in the Built-In Render Pipeline
Indirect & Procedural Rendering in Shader Graph
on the Unity Discussions site if you use URP or HDRP.
Additional resources
Choose a method for optimizing draw calls


---

<!-- source=unity_docs; title=The camera view; url=https://docs.unity3d.com/6000.4/Documentation/Manual/CameraView.html -->

# The camera view

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/CameraView.html

Cameras
The camera view
The camera view
Resources about the view frustum, and techniques for changing or moving the
camera
A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture.
More info
See in
Glossary
view.
Page
Description
Introduction to the camera view
Learn about the shape of the region the camera views, including the view frustum and
clipping planes
A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane.
More info
See in
Glossary
.
Make the camera perspective oblique
Set the view frustum so that one side extends at a shallower angle, for example to increase the feeling of speed.
Calculate the size of the frustum at a distance
Get the size and shape of the frustum rectangle at a distance from the camera.
CameraRays
Resources about calculating and using lines that point from the camera to positions in world space.
Additional resources
Set the camera background with Clear Flags in the Built-In Render Pipeline


---

<!-- source=unity_docs; title=Lighting data; url=https://docs.unity3d.com/6000.4/Documentation/Manual/Lightmap-data-landing.html -->

# Lighting data

- Source: unity_docs
- Section: Manual
- URL: https://docs.unity3d.com/6000.4/Documentation/Manual/Lightmap-data-landing.html

Lighting
Direct and indirect lighting
Lighting data
Lighting data
Resources for how Unity stores lighting data and visibility data for lightmapping,
Light Probes
Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space.
More info
See in
Glossary
, and
Reflection Probes
A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials.
More info
See in
Glossary
.
Page
Description
Introduction to lighting data
Understand how Unity stores lighting data and visibility data for lightmapping, Light Probes, and Reflection Probes.
Lighting Data Assets
Learn about the asset Unity creates to store precomputed lighting data for a
scene
A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces.
More info
See in
Glossary
.
GI cache
The cached intermediate files used when Unity precomputes lighting data. Unity keeps this cache to speed up computation.
More info
See in
Glossary
Learn about the internal data cache Unity uses to store intermediate files when it precomputes lighting data for lightmapping.
Lightmap data format
Understand how Unity stores light intensity as textures during lightmapping, and learn about support for high dynamic range (HDR)
lightmaps
A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting.
More info
See in
Glossary
.
Light Probe data format
Understand how Unity stores light as spherical harmonics data in Light Probes.
