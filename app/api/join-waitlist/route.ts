import { NextResponse } from "next/server"

export async function POST(request: Request) {
  try {
    const formData = await request.json()
    
    console.log("Received form data:", formData)

    const response = await fetch(`${process.env.N8N_WEBHOOK_URL}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })

    console.log("n8n Response Status:", response.status)
    console.log("n8n response", response)

    if (!response.ok) {
      throw new Error("Failed to submit to n8n")
    }

    const data = await response.json().catch(() => ({}))

    console.log('response json', data)

    return NextResponse.json({ 
      success: true, 
      waitlist_count: data.total_waitlist || 0 
    }, { status: 200 })
  } catch (error) {
    console.error("API Route Error:", error)
    return NextResponse.json({ success: false, error: "Failed to submit form" }, { status: 500 })
  }
}