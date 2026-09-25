from pathlib import Path

IMMUTABLE = {
 "immigration_logo": Path("assets/official/immigration-logo.png"),
 "coat_of_arms": Path("assets/official/tanzania-coat-of-arms.png"),
 "mjy_logo": Path("assets/official/mjue-jirani-yako-logo.png"),
}
PASSPORTS = {
 "ordinary": Path("assets/passports/ordinary-blue.png"),
 "service": Path("assets/passports/service-green.png"),
 "diplomatic": Path("assets/passports/diplomatic-red.png"),
}

def require_exact_asset(kind):
    table={**IMMUTABLE,**PASSPORTS}
    if kind not in table: raise KeyError("Unknown approved asset: "+kind)
    p=table[kind]
    if not p.is_file(): raise FileNotFoundError(f"Exact approved asset missing: {kind} -> {p}")
    return p

def generation_instruction(kind):
    require_exact_asset(kind)
    return f"{kind} is compositor-only. Never ask diffusion to recreate it."
