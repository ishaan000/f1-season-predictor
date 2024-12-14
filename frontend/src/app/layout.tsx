export const metadata = {
  title: "F1 Season Predictor",
  description: "An app that predicts F1 season standings and outcomes.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
