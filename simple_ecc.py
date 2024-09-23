class EllipticCurve:
    """
    Simple implementation of an elliptic curve defined by the equation:
    y^2 = x^3 + ax + b over a finite field with prime modulus p.
    """

    def __init__(self, a, b, p):
        self.a = a  # Coefficient of x
        self.b = b  # Constant term
        self.p = p  # Prime modulus

    def is_on_curve(self, point):
        """
        Check if a given point (x, y) lies on the elliptic curve.
        """
        if point is None:
            return True
        x, y = point
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def point_add(self, P, Q):
        """
        Add two points P and Q on the elliptic curve.
        """
        if P is None:
            return Q
        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        if P == Q:
            return self.point_double(P)

        if x1 == x2 and y1 != y2:
            return None  # Point at infinity

        # Calculate the slope (lambda)
        lam = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p

        # Calculate the new point
        x3 = (lam**2 - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def point_double(self, P):
        """
        Double a point P on the elliptic curve.
        """
        if P is None:
            return None

        x1, y1 = P

        lam = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p) % self.p

        x3 = (lam**2 - 2 * x1) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def scalar_multiply(self, P, n):
        """
        Perform scalar multiplication: n * P, where P is a point on the curve.
        """
        Q = None  # Initialize Q as the point at infinity
        while n > 0:
            if n % 2 == 1:
                Q = self.point_add(Q, P)  # Add P to Q if the current bit of n is 1
            P = self.point_double(P)  # Double P at each step
            n //= 2
        return Q


def main():
    # Define an elliptic curve over a finite field
    # Curve parameters: y^2 = x^3 + 2x + 3 over field of prime p = 97
    a = 2
    b = 3
    p = 97
    curve = EllipticCurve(a, b, p)

    # Define a point on the curve
    G = (3, 6)  # A point on the curve

    # Check if the point lies on the curve
    if curve.is_on_curve(G):
        print(f"Point {G} lies on the curve.")
    else:
        print(f"Point {G} does not lie on the curve.")

    # Perform scalar multiplication (k * G)
    k = 5
    result = curve.scalar_multiply(G, k)
    print(f"{k} * G = {result}")

    # Check if the result lies on the curve
    if curve.is_on_curve(result):
        print(f"The result {result} lies on the curve.")
    else:
        print(f"The result {result} does not lie on the curve.")


if __name__ == "__main__":
    main()
