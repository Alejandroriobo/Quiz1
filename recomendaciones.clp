(deffunction calcular-destino (?preferencia ?presupuesto)
   (if (and (eq ?preferencia "playa") (>= ?presupuesto 1000))
       then return "Cancún"
       else if (and (eq ?preferencia "montaña") (>= ?presupuesto 800))
           then return "Andes"
           else return "No disponible"
   )
)

(deftemplate recomendacion
   (slot destino)
)

(defrule recomendar-destino
   (preferencia ?p)
   (presupuesto ?b)
   =>
   (bind ?destino (calcular-destino ?p ?b))
   (assert (recomendacion (destino ?destino)))
)
