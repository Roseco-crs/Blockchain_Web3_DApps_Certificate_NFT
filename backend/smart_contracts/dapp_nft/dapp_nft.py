import beaker as bk 
import pyteal as pt 
from utils import generate_complete_certificate
import os

class MyState:
    result = bk.GlobalStateValue(pt.TealType.uint64)

# App Initialize 
app = bk.Application("dapp_nft", state= MyState())


def Welcome(name: pt.abi.String, *, output: pt.abi.String) -> pt.Expr:
    return output.set(pt.Concat(pt.Bytes(" Welcome, "), name.get()))
    
def create_asset():
    pass

def connect_to_account():
    pass

def nft_generation():
    pass



if __name__ == "__main__" :
    spec = app.build()
    spec.export("artifacts")

