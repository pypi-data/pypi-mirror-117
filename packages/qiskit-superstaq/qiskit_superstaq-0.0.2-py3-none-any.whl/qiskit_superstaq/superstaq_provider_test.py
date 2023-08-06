import codecs
import pickle
from unittest.mock import MagicMock, patch

import qiskit

import qiskit_superstaq as qss


def test_provider() -> None:
    ss_provider = qss.superstaq_provider.SuperstaQProvider(access_token="MY_TOKEN")

    assert str(ss_provider.get_backend("ibmq_qasm_simulator")) == str(
        qss.superstaq_backend.SuperstaQBackend(
            provider=ss_provider,
            url=qss.API_URL,
            backend="ibmq_qasm_simulator",
        )
    )

    assert str(ss_provider) == "<SuperstaQProvider(name=superstaq_provider)>"

    assert (
        repr(ss_provider) == "<SuperstaQProvider(name=superstaq_provider, access_token=MY_TOKEN)>"
    )

    backend_names = [
        "aqt_device",
        "ionq_device",
        "rigetti_device",
        "ibmq_botoga",
        "ibmq_casablanca",
        "ibmq_jakarta",
        "ibmq_qasm_simulator",
    ]

    backends = []
    for name in backend_names:
        backends.append(
            qss.superstaq_backend.SuperstaQBackend(
                provider=ss_provider, url=qss.API_URL, backend=name
            )
        )

    assert ss_provider.backends() == backends


@patch("requests.post")
def test_aqt_compile(mock_post: MagicMock) -> None:
    provider = qss.superstaq_provider.SuperstaQProvider(access_token="MY_TOKEN")

    qc = qiskit.QuantumCircuit(8)
    qc.cz(4, 5)

    out_qasm_str = """OPENQASM 2.0;\ninclude "qelib1.inc";\n\n\n//"""
    out_qasm_str += """Qubits: [4, 5]\nqreg q[2];\n\n\ncz q[0],q[1];\n"""

    mock_post.return_value.json = lambda: {
        "qasm_str": out_qasm_str,
        "state_jp": codecs.encode(pickle.dumps({}), "base64").decode(),
        "pulse_list_jp": codecs.encode(pickle.dumps({}), "base64").decode(),
    }

    expected_qc = qiskit.QuantumCircuit(2)
    expected_qc.cz(0, 1)
    assert provider.aqt_compile(qc).circuit == expected_qc
