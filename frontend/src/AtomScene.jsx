import React, {useMemo} from "react";
import {Canvas} from "@react-three/fiber";
import {OrbitControls, Stars} from "@react-three/drei";
import * as THREE from "three";

function Lattice({kind="silicon"}) {
  const points=useMemo(()=>{
    const p=[];
    const n=kind==="graphene"?5:3;
    for(let x=-n;x<=n;x++) for(let y=-n;y<=n;y++) for(let z=-n;z<=n;z++){
      if(kind==="graphene" && z!==0) continue;
      if(kind==="graphene" && (x+y)%2!==0) continue;
      if(kind!=="graphene" && (x+y+z)%2!==0) continue;
      p.push([x*(kind==="graphene"?.58:.8),y*(kind==="graphene"?.58:.8),z*.8]);
    }
    return p;
  },[kind]);
  const color=kind==="copper"?"#e5a05b":kind==="graphene"?"#65d6c2":"#78b8ff";
  return <group>{points.map((p,i)=><mesh key={i} position={p}><sphereGeometry args={[.13,18,18]}/><meshStandardMaterial color={color} metalness={.45} roughness={.25}/></mesh>)}
  {points.filter((_,i)=>i%3===0).map((p,i)=><mesh key={"b"+i} position={p}><sphereGeometry args={[.19,12,12]}/><meshBasicMaterial color={color} transparent opacity={.12}/></mesh>)}</group>;
}
export default function AtomScene({kind="silicon"}) {
 return <div className="scene"><Canvas camera={{position:[5,4,7],fov:42}}><ambientLight intensity={1.2}/><pointLight position={[5,5,5]} intensity={45}/><pointLight position={[-5,-3,-4]} color="#2c9fff" intensity={20}/><Stars radius={40} depth={20} count={900} factor={2} fade/><Lattice kind={kind}/><OrbitControls enablePan={false} minDistance={3} maxDistance={14} autoRotate autoRotateSpeed={.45}/></Canvas></div>;
}
