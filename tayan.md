Sistema do jogo de adivinhação

```mermaid
graph LR
A[Computador] --> B(Pensa em um número entre 0 e 20)
B --> C(Acerto)
B --> D(Erro)
C --> E{Ganha-se 5 reais}
D --> F{Perde-se 5 reais}
```
