```mermaid
flowchart TD
    A[Usuario] --> B{Tipo de Operación}

    B --> C[Ingreso]
    B --> D[Egreso]
    B --> E[Transferencia<br/>entre cuentas propias]
    B --> F[Préstamo]
    B --> G[Pago Cuota Contrato]
    B --> H[Compra de Bien]

    C --> C1[insert_financial_movement]
    D --> D1[insert_financial_movement]
    E --> E1[insert_financial_movement]

    C1 --> M[(MOVIMIENTOS_FINANCIEROS)]
    D1 --> M
    E1 --> M

    C1 --> CT1[(CUENTAS_FINANCIERAS<br/>+ saldo])]
    D1 --> CT2[(CUENTAS_FINANCIERAS<br/>- saldo])]
    E1 --> CT3[(CUENTAS_FINANCIERAS<br/>- origen / + destino)]

    C -.opcional.-> EMP1{"¿Tiene<br/>Emprendimiento?"}
    D -.opcional.-> EMP1
    EMP1 -->|Sí| EMP2[recalcular_emprendimiento]
    EMP2 --> EM[(EMPRENDIMIENTOS<br/>Ingresos/Gastos/Margen)]

    F --> F1[insert_financial_movement_con_prestamo]
    F1 --> M
    F1 --> CT4[(CUENTAS_FINANCIERAS<br/>ajusta saldo)]
    F1 --> P[(PRESTAMOS<br/>crea o actualiza saldo)]

    G --> G1[insert_egreso_con_contrato]
    G1 --> M
    G1 --> CT5[(CUENTAS_FINANCIERAS<br/>- saldo)]
    G1 --> CO[(CONTRATOS<br/>Monto Cancelado /<br/>Saldo Pendiente)]

    H --> H1[insert_bien_con_movimiento]
    H1 -->|Si se pagó con cuenta| M
    H1 -->|Si se pagó con cuenta| CT6[(CUENTAS_FINANCIERAS<br/>- saldo)]
    H1 --> BI[(BIENES<br/>Valor Actual)]

    CT1 & CT2 & CT3 & CT4 & CT5 & CT6 & P & CO & BI --> PAT[calcular_patrimonio]

    PAT --> PAT1["Activos = Cuentas + Bienes<br/>+ Préstamos Por Cobrar"]
    PAT --> PAT2["Pasivos = Préstamos Por Pagar<br/>+ Saldo Pendiente Contratos"]
    PAT1 --> NETO[Patrimonio Neto]
    PAT2 --> NETO

    NETO --> DASH[Dashboard Textual]
    NETO --> SNAP[Snapshot Patrimonial]
    NETO --> KPI[KPIs]

    P --> ALERT[get_alertas_text]
    CO --> ALERT
    ALERT --> ALERT2["Detecta mora:<br/>último pago vs hoy > 30 días"]
    ALERT2 --> DASH
```
