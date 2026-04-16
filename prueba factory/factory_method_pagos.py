"""
Patrón Factory Method - Sistema de Procesamiento de Pagos

Caso Real: Una tienda online que acepta múltiples métodos de pago
(tarjeta de crédito, PayPal, transferencia bancaria).

El patrón permite agregar nuevos métodos de pago sin modificar 
el código existente de procesamiento de órdenes.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict


# ==================== PRODUCTOS ====================

class MetodoPago(ABC):
    """
    Interfaz que define cómo debe comportarse cualquier método de pago.
    Todos los métodos de pago deben implementar estas operaciones.
    """
    
    @abstractmethod
    def procesar_pago(self, monto: float, datos: Dict) -> bool:
        """Procesa el pago y retorna True si fue exitoso"""
        pass
    
    @abstractmethod
    def obtener_comision(self, monto: float) -> float:
        """Calcula la comisión del método de pago"""
        pass
    
    @abstractmethod
    def generar_recibo(self, monto: float) -> str:
        """Genera el recibo de la transacción"""
        pass

# ==================== CONCRETOS ====================

class PagoTarjetaCredito(MetodoPago):
    """Implementación concreta para pagos con tarjeta de crédito"""
    
    def procesar_pago(self, monto: float, datos: Dict) -> bool:
        numero_tarjeta = datos.get('numero_tarjeta', '')
        cvv = datos.get('cvv', '')
        
        # Simulación de validación
        if len(numero_tarjeta) == 16 and len(cvv) == 3:
            print(f"💳 Procesando pago con tarjeta terminada en {numero_tarjeta[-4:]}")
            print(f"   Monto: ${monto:.2f}")
            print(f"   ✓ Pago autorizado")
            return True
        else:
            print("   ✗ Tarjeta inválida")
            return False
    
    def obtener_comision(self, monto: float) -> float:
        return monto * 0.029  # 2.9% de comisión
    
    def generar_recibo(self, monto: float) -> str:
        return f"""
        ═══════════════════════════════
        RECIBO DE PAGO - TARJETA
        ═══════════════════════════════
        Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        Monto: ${monto:.2f}
        Comisión: ${self.obtener_comision(monto):.2f}
        Total: ${monto + self.obtener_comision(monto):.2f}
        ═══════════════════════════════
        """


class PagoPayPal(MetodoPago):
    """Implementación concreta para pagos con PayPal"""
    
    def procesar_pago(self, monto: float, datos: Dict) -> bool:
        email = datos.get('email', '')
        
        if '@' in email:
            print(f"🅿️  Procesando pago con PayPal")
            print(f"   Email: {email}")
            print(f"   Monto: ${monto:.2f}")
            print(f"   ✓ Pago completado")
            return True
        else:
            print("   ✗ Email de PayPal inválido")
            return False
    
    def obtener_comision(self, monto: float) -> float:
        return monto * 0.034 + 0.30  # 3.4% + $0.30
    
    def generar_recibo(self, monto: float) -> str:
        return f"""
        ═══════════════════════════════
        RECIBO DE PAGO - PAYPAL
        ═══════════════════════════════
        Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        Monto: ${monto:.2f}
        Comisión: ${self.obtener_comision(monto):.2f}
        Total: ${monto + self.obtener_comision(monto):.2f}
        ═══════════════════════════════
        """


class PagoTransferencia(MetodoPago):
    """Implementación concreta para pagos por transferencia bancaria"""
    
    def procesar_pago(self, monto: float, datos: Dict) -> bool:
        cuenta = datos.get('numero_cuenta', '')
        banco = datos.get('banco', '')
        
        if len(cuenta) >= 10:
            print(f"🏦 Procesando transferencia bancaria")
            print(f"   Banco: {banco}")
            print(f"   Cuenta: ****{cuenta[-4:]}")
            print(f"   Monto: ${monto:.2f}")
            print(f"   ✓ Transferencia iniciada (procesa en 24-48hs)")
            return True
        else:
            print("   ✗ Número de cuenta inválido")
            return False
    
    def obtener_comision(self, monto: float) -> float:
        return 5.00  # Comisión fija
    
    def generar_recibo(self, monto: float) -> str:
        return f"""
        ═══════════════════════════════
        RECIBO - TRANSFERENCIA BANCARIA
        ═══════════════════════════════
        Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        Monto: ${monto:.2f}
        Comisión: ${self.obtener_comision(monto):.2f}
        Total: ${monto + self.obtener_comision(monto):.2f}
        Tiempo estimado: 24-48 horas
        ═══════════════════════════════
        """


# ==================== CREADORES ====================

class ProcesadorPago(ABC):
    """
    Clase base que define el Factory Method.
    
    La responsabilidad principal NO es crear métodos de pago,
    sino procesar órdenes de compra usando el método de pago apropiado.
    """
    
    @abstractmethod
    def crear_metodo_pago(self) -> MetodoPago:
        """Factory Method: cada subclase decide qué método de pago crear"""
        pass
    
    def procesar_orden(self, monto: float, datos_pago: Dict) -> None:
        """
        Lógica de negocio que usa el Factory Method.
        
        Este método es el mismo para todos los procesadores,
        pero cada uno crea un método de pago diferente.
        """
        print("\n" + "="*50)
        print("PROCESANDO NUEVA ORDEN")
        print("="*50)
        
        # Usar el Factory Method para obtener el método de pago apropiado
        metodo = self.crear_metodo_pago()
        
        # Procesar el pago
        if metodo.procesar_pago(monto, datos_pago):
            # Generar y mostrar el recibo
            print(metodo.generar_recibo(monto))
            print("✓ Orden completada exitosamente\n")
        else:
            print("\n✗ Error al procesar el pago\n")


class ProcesadorTarjeta(ProcesadorPago):
    """Procesador específico para tarjetas de crédito"""
    
    def crear_metodo_pago(self) -> MetodoPago:
        return PagoTarjetaCredito()


class ProcesadorPayPal(ProcesadorPago):
    """Procesador específico para PayPal"""
    
    def crear_metodo_pago(self) -> MetodoPago:
        return PagoPayPal()

class ProcesadorTransferencia(ProcesadorPago):
    """Procesador específico para transferencias bancarias"""
    
    def crear_metodo_pago(self) -> MetodoPago:
        return PagoTransferencia()


# ==================== CÓDIGO CLIENTE ====================

def procesar_compra(procesador: ProcesadorPago, monto: float, datos: Dict) -> None:
    """
    El código cliente trabaja con procesadores a través de su interfaz base.
    
    No necesita saber qué tipo específico de procesador está usando.
    Esto permite cambiar el método de pago sin modificar este código.
    """
    procesador.procesar_orden(monto, datos)

if __name__ == "__main__":
    print("🛒 SISTEMA DE PROCESAMIENTO DE PAGOS")
    print("="*50)
    
    # Ejemplo 1: Pago con tarjeta de crédito
    procesador_tarjeta = ProcesadorTarjeta()
    procesar_compra(procesador_tarjeta,  150.00,
        {
            'numero_tarjeta': '4532015112830366',
            'cvv': '123',
            'titular': 'Juan Pérez'
        }
    )
    
    # Ejemplo 2: Pago con PayPal
    procesador_paypal = ProcesadorPayPal()
    procesar_compra(
        procesador_paypal,
        89.99,
        {
            'email': 'cliente@email.com'
        }
    )
    
    # Ejemplo 3: Pago con transferencia bancaria
    procesador_transferencia = ProcesadorTransferencia()
    procesar_compra(
        procesador_transferencia,
        500.00,
        {
            'numero_cuenta': '1234567890123456',
            'banco': 'Banco Nacional'
        }
    )
    
    print("\n" + "="*50)
    print("VENTAJAS DEL PATRÓN:")
    print("="*50)
    print("✓ Agregar nuevos métodos de pago sin modificar código existente")
    print("✓ Cada método de pago encapsula su propia lógica")
    print("✓ El código cliente es independiente de los métodos concretos")
    print("✓ Fácil de testear y mantener")