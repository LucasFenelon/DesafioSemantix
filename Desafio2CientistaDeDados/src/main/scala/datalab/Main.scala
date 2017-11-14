package datalab

import scala.io.Source._
import scala.runtime.ZippedTraversable2.zippedTraversable2ToTraversable

object grafoMain {
  def main(args: Array[String]){
    val edge = fromFile("C:/Users/lgomesf/workspace/teste/Semantix2/src/main/scala/Documents/edges_").mkString
    
    edge.split("\n").array.foreach{
      row =>
        var verticeX : Array[Double] = Array[Double]()// = 0.0
        var verticeY : Array[Double] = Array[Double]()
        var i = 0 
        
        row.trim.split(" ").array.foreach{col =>
          if (i == 0) {
              verticeX :+ col.toDouble
              i = i + 1
          }else{ 
            verticeY :+ col.toDouble
          }
        }
        
        print(s"*** para vertices ${verticeX.toString} e ${verticeY.toString} *** \n")
        print(s"distanciaAbsol -> ${distanciaAbsol[Double, Double](verticeX, verticeY).toString} \n")
        print(s"distanceBetweenTwoVectors -> ${distanceBetweenTwoVectors[Double, Double](verticeX, verticeY).toString} \n")
        print(s"cosineOfDistanceBetweenTwoVectors -> ${cosineOfDistanceBetweenTwoVectors[Double, Double](verticeX, verticeY).toString} \n")
    }
  }
  
  def distanciaAbsol[T <% Double, U <% Double](x: Array[T], y: Array[U]): 
    Double = (x, y).zipped.foldLeft(0.0)((s, t) => s + Math.abs(t._1 - t._2))
    
  def distanceBetweenTwoVectors[T <% Double, U <% Double](x: Array[T], y: Array[U]): 
    Double =  Math.sqrt((x, y).zipped.foldLeft(0.0)((s, t) => { val d = t._1 - t._2; s + d*d} ))
    
  def cosineOfDistanceBetweenTwoVectors[T <% Double, U <% Double](x: Array[T], y: Array[U]): Double = {
    val zeros = (0.0, 0.0, 0.0)
    val norms = (x, y).zipped.foldLeft(zeros)((s, t) => 
      (s._1 + t._1*t._2, s._2 + t._1*t._1, s._3 + t._2*t._2))  
      norms._1/Math.sqrt(norms._2*norms._3)
  }
}