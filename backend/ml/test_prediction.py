from predict import predict_risk


sample = [
    2,
    180,
    90,
    35,
    180,
    32.5,
    0.8,
    45,
]


result = predict_risk(
    sample
)

print(result)