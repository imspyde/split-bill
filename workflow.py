from dagflows.authoring import Workflow
from dagflows.runtime import Ctx

wf = Workflow("split-bill")


@wf.node()
def split_bill(ctx: Ctx) -> dict:
    bill = 2400
    tip_percent = 10
    people = 4

    total = bill + (bill * tip_percent / 100)
    per_person = total / people

    ctx.log.info(f"Total: {total:,.0f}; per person: {per_person:,.0f}")

    return {"total": total, "per_person": per_person}
