from qiskit import IBMQ
IBMQ.save_account('6b30a3a191b3bfd1bb47853df2add9cb902fca77ef37a07560fac6e11007c9c4336b449600a2e387ee662814d58fe539933da5b210dd6df1dc0b2d9ccae93bdf');
from qiskit import QuantumCircuit, execute, Aer


# 하나의 회로 전용 인스턴스 생성
circ = QuantumCircuit(n_input,n_output)

# 양자회로는 항상 측정게이트로 끝남
# 측정게이트
circ.measure(i,j)

# 만든 양자회로 시각화(출력)
circ.draw(output='mpl',justify='none')