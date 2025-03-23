import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';


const loader = new GLTFLoader();

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setClearColor(0xffffff);

document.body.appendChild(renderer.domElement);

// Create a new Stats object
var stats = new Stats();
stats.showPanel( 1 ); // 0: fps, 1: ms, 2: mb, 3+: custom
document.body.appendChild( stats.dom );

// Create a directional light
const light = new THREE.DirectionalLight(0xffffff, 0.5);
light.position.set(1, 1, 1);
scene.add(light);

// Create OrbitControls
const controls = new OrbitControls(camera, renderer.domElement);
controls.update();

var vector3D = new THREE.Vector3(0, 0, 0);

loader.load(
    // resource URL
    './bocage.gltf',
    // called when the resource is loaded
    function (gltf) {
        scene.add(gltf.scene);

        gltf.scene.traverse(function (object) {
            console.log(object);
        });

        const box = new THREE.Box3().setFromObject(gltf.scene);
        const center = box.getCenter(new THREE.Vector3());
        console.log(center);
        vector3D = center;
        
        // Translate the object
        gltf.scene.position.x = -center.x;
        gltf.scene.position.y = -center.y;
        gltf.scene.position.z = -center.z;
        
        animate();
    },
    // called while loading is progressing
    function (xhr) {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
    },
    // called when loading has errors
    function (error) {
        console.log('An error happened');
    }
);

/*
loader.load(
    // resource URL
    './bocage_sud.gltf',
    // called when the resource is loaded
    function (gltf) {
        scene.add(gltf.scene);

        const box = new THREE.Box3().setFromObject(gltf.scene);
        const center = box.getCenter(new THREE.Vector3());
        console.log(center);
        
        // Translate the object
        gltf.scene.position.x = -vector3D.x;
        gltf.scene.position.y = -vector3D.y;
        gltf.scene.position.z = -vector3D.z;     

        animate();
    },
    // called while loading is progressing
    function (xhr) {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded');
    },
    // called when loading has errors
    function (error) {
        console.log('An error happened');
    }
);*/

camera.position.z = 5;

function animate() {
    stats.begin();

    renderer.render(scene, camera);

    stats.end();

	requestAnimationFrame(animate);	
}

animate();