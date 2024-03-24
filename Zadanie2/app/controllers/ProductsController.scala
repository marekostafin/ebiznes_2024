package controllers

import javax.inject._
import play.api._
import play.api.mvc._

/**
 * This controller creates an `Action` to handle HTTP requests to the
 * application's home page.
 */
@Singleton
class ProductsController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  var db: List[String] = List("Twilight Imperium", "Oath", "Gloomhaven", "Ticket to Ride", "Catan", "Root", "Codenames")

  def index() = Action { implicit request: Request[AnyContent] =>
    Ok(views.html.index())
  }

  def getProductById(id: Int): Action[AnyContent] = Action {
    db.lift(id) match {
      case Some(value) => Ok(value)
      case None => NotFound("Nie znaleziono produktu")
    }
  }

  def getAllProducts: Action[AnyContent] = Action {
    Ok(db.toString())
  }

  def updateProduct(id: Int, update: String): Action[AnyContent] = Action {
    db.lift(id) match {
      case Some(old) =>
        db = db.updated(id, update)
        Ok("Zamieniono wartość " + old + " na " + update )
      case None => NotFound("Nie znaleziono produktu o id " + id)
    }
  }

  def deleteProduct(id: Int): Action[AnyContent] = Action {
    db.lift(id) match {
      case Some(old) =>
        db = db.filterNot(_ == db(id))
        Ok("Usunięto wartość " + old + " z bazy produktów")
      case None => NotFound("Nie znaleziono produktu o id " + id)
    }
  }

  def addProduct(product: String): Action[AnyContent] = Action {
    db = db.appended(product)
    Ok("Dodano " + product + " do bazy produktów")
  }

}
